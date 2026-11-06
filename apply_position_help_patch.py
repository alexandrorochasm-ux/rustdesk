import os
import re

print("=== APLICANDO PERSONALIZACAO POSITION HELP ===")

base_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Configurações de Servidor e Chave em hbb_common/src/config.rs
config_rs = os.path.join(base_dir, 'libs', 'hbb_common', 'src', 'config.rs')
if os.path.exists(config_rs):
    with open(config_rs, 'r', encoding='utf-8') as f:
        content = f.read()

    # Atualiza Servidor Rendezvous
    content = re.sub(
        r'pub const RENDEZVOUS_SERVERS: &\[&str\] = &\[.*?\];',
        'pub const RENDEZVOUS_SERVERS: &[&str] = &["suporte.position.com.br"];',
        content
    )

    # Atualiza Chave Pública
    content = re.sub(
        r'pub const RS_PUB_KEY: &str = ".*?";',
        'pub const RS_PUB_KEY: &str = "pDGH1GdajITwKK04YUrPFbLdr6if1GbiRI8ps7lMEJc=";',
        content
    )

    # Atualiza Nome do App
    content = re.sub(
        r'pub static ref APP_NAME: RwLock<String> = RwLock::new\(".*?"\.to_owned\(\)\);',
        'pub static ref APP_NAME: RwLock<String> = RwLock::new("Position Help".to_owned());',
        content
    )

    with open(config_rs, 'w', encoding='utf-8') as f:
        f.write(content)
    print("libs/hbb_common/src/config.rs atualizado com sucesso!")
else:
    print(f"AVISO: {config_rs} não encontrado localmente (será aplicado no checkout do submodule).")

# 2. Atualiza títulos e constantes do Flutter
consts_dart = os.path.join(base_dir, 'flutter', 'lib', 'consts.dart')
if os.path.exists(consts_dart):
    with open(consts_dart, 'r', encoding='utf-8') as f:
        c_dart = f.read()

    c_dart = re.sub(r'const String kEnvPortableExecutable = ".*?";', 'const String kEnvPortableExecutable = "POSITION_HELP_APPNAME";', c_dart)

    with open(consts_dart, 'w', encoding='utf-8') as f:
        f.write(c_dart)
    print("flutter/lib/consts.dart atualizado com sucesso!")

print("=== PATCH POSITION HELP FINALIZADO COM SUCESSO ===")

