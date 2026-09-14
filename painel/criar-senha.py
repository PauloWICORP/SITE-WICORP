#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cria ou troca a senha do painel. Rode uma vez, no servidor."""

import getpass
import json
import os
import pathlib
import secrets
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from app import CONFIG, cfg_ler, hash_senha  # noqa: E402


def main():
    atual = cfg_ler()
    if atual:
        print(f"Já existe uma senha para o usuário '{atual['usuario']}'.")
        if input("Trocar? (s/N) ").strip().lower() != "s":
            return

    usuario = input("Usuário [admin]: ").strip() or "admin"

    while True:
        senha = getpass.getpass("Senha (mínimo 12 caracteres): ")
        if len(senha) < 12:
            print("  Curta demais. Use pelo menos 12 caracteres.\n")
            continue
        if senha != getpass.getpass("Repita a senha: "):
            print("  As senhas não conferem.\n")
            continue
        break

    sal, h = hash_senha(senha)
    CONFIG.write_text(json.dumps({
        "usuario": usuario,
        "sal": sal,
        "hash": h,
        "segredo": (atual or {}).get("segredo") or secrets.token_urlsafe(48),
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    os.chmod(CONFIG, 0o600)

    print(f"\nPronto. Arquivo: {CONFIG}")
    print("A senha não fica guardada — só o hash. Se esquecer, rode este script de novo.")


if __name__ == "__main__":
    main()
