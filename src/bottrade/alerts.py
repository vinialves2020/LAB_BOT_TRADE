from __future__ import annotations

import logging

import httpx

LOGGER = logging.getLogger(__name__)


class TelegramAlerter:
    def __init__(self, bot_token: str, chat_id: str, timeout_seconds: int = 15) -> None:
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.timeout_seconds = timeout_seconds

    @property
    def configured(self) -> bool:
        return bool(self.bot_token and self.chat_id)

    def send(self, message: str) -> bool:
        if not self.configured:
            LOGGER.info("Telegram is not configured; alert was logged only: %s", message)
            return False
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        chunks = [message[index : index + 3900] for index in range(0, len(message), 3900)]
        try:
            with httpx.Client(timeout=self.timeout_seconds) as client:
                for chunk in chunks:
                    response = client.post(
                        url,
                        json={
                            "chat_id": self.chat_id,
                            "text": chunk,
                            "disable_web_page_preview": True,
                        },
                    )
                    response.raise_for_status()
            return True
        except (httpx.HTTPError, ValueError) as exc:
            # httpx error strings can contain the request URL, which embeds the bot token.
            LOGGER.error("Telegram alert failed (%s); request details redacted", type(exc).__name__)
            return False

    def exception(self, job: str, exc: BaseException) -> bool:
        return self.send(
            f"🚨 BOT_TRADE — falha em {job}\n{type(exc).__name__}; "
            "consulte os logs protegidos para o diagnóstico."
        )
