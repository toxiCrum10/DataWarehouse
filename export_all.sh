#!/bin/bash

# Nastav premenné
PROJECT_ID="nicolips"
EXPORT_DIR="$HOME/data-warehouse/export"
mkdir -p "$EXPORT_DIR"

# Získaj zoznam datasetov
DATASETS=$(bq ls --project_id="$PROJECT_ID" --format=prettyjson | jq -r '.[].datasetReference.datasetId')

# Pre každý dataset
for dataset in $DATASETS; do
  echo "🔹 Dataset: $dataset"
bq query --use_legacy_sql=false --format=csv \
      "SELECT * FROM \`$PROJECT_ID.$dataset.$table\`" > "$OUTFILE"
  # Získaj zoznam tabuliek v datasete
  TABLES=$(bq ls "$PROJECT_ID:$dataset" | awk 'NR>2 {print $1}')

  for table in $TABLES; do
    echo "  ↳ Exportujem tabuľku: $table"
    OUTFILE="$EXPORT_DIR/${dataset}_${table}.csv"
    
    bq query --use_legacy_sql=false --format=csv \
      "SELECT * FROM \`$PROJECT_ID.$dataset.$table\`" > "$OUTFILE"
  done
done

echo " Export hotový: všetky CSV sú v $EXPORT_DIR"

