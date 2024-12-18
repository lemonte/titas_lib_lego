#!/bin/bash

# Diretório do código-fonte
DIRETORIO="titas_lib"
ARQUIVO_SAIDA="resultado.py"

# Lista dos arquivos em ordem específica
ORDENACAO=(
    "falar_erro.py"
    "robo_imports.py"
    "acoes_robo.py"
    "cor_robo.py"
    "hub_robo.py"
    "hub_base.py"
    "robo_motor.py"
    "robo_brick.py"
    "seguidor.py"
    "sensores_robo.py"
    "static_property.py"
)

# Limpa o arquivo de saída, se existir
> "$ARQUIVO_SAIDA"

# Arquivos temporários para separar imports e código
TEMP_IMPORTS=$(mktemp)
TEMP_CODIGO=$(mktemp)

# Processar cada arquivo na ordem definida
for arquivo in "${ORDENACAO[@]}"; do
    caminho_arquivo="$DIRETORIO/$arquivo"

    if [[ -f "$caminho_arquivo" ]]; then
        # Extrair imports válidos e adicioná-los ao temporário (exceto "from titas_lib.")
        grep -E "^import |^from " "$caminho_arquivo" | grep -Ev "^from titas_lib\.|^import titas_lib" >> "$TEMP_IMPORTS"

        # Extrair o restante do código e adicionar ao temporário
        echo "" >> "$TEMP_CODIGO"
        echo "# Código de $arquivo" >> "$TEMP_CODIGO"
        sed '/^import /d;/^from /d' "$caminho_arquivo" >> "$TEMP_CODIGO"
    else
        echo "Aviso: Arquivo $arquivo não encontrado no diretório $DIRETORIO." >&2
    fi
done

# Adicionar imports ao arquivo de saída
echo "# Consolidated Imports" >> "$ARQUIVO_SAIDA"
sort -u "$TEMP_IMPORTS" >> "$ARQUIVO_SAIDA"
echo "" >> "$ARQUIVO_SAIDA"

# Adicionar código consolidado ao arquivo de saída
echo "# Consolidated Code" >> "$ARQUIVO_SAIDA"
cat "$TEMP_CODIGO" >> "$ARQUIVO_SAIDA"

# Limpar arquivos temporários
rm "$TEMP_IMPORTS" "$TEMP_CODIGO"

echo "Consolidação completa! Arquivo gerado: $ARQUIVO_SAIDA"
