#!/bin/bash
echo "Refreshing all card sets in card_set_lookup/"
for FILE in card_set_lookup/*.json; do
    SET_ID=$(basename "$FILE" .json)
    echo "Updating set: $SET_ID"
    curl "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" -o "$FILE"
    echo "Data written to: $FILE"
done
echo "All card sets refreshed."