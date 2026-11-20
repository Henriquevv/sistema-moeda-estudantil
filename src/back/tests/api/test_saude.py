"""Testes da rota de saúde, usada para conferir qual commit está publicado."""

from fastapi import status
from fastapi.testclient import TestClient

from app.config import settings


def test_saude_informa_que_a_api_esta_no_ar_e_a_versao_publicada(
    cliente_api: TestClient, monkeypatch
):
    """A rota responde ok e devolve o commit que a Render informa em RENDER_GIT_COMMIT."""
    monkeypatch.setattr(settings, "RENDER_GIT_COMMIT", "abc1234")

    res = cliente_api.get("/saude")

    assert res.status_code == status.HTTP_200_OK
    assert res.json() == {"status": "ok", "versao": "abc1234"}


def test_saude_usa_local_quando_nao_ha_commit_informado(cliente_api: TestClient):
    """Fora da Render (Docker local e testes) a versão aparece como local."""
    assert cliente_api.get("/saude").json()["versao"] == "local"
