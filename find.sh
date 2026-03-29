for f in '/Applications/Monster Prom 4 Monster Con.app/Contents/Resources/Data/StreamingAssets/aa/StandaloneOSX/'*.bundle ~/Desktop/monsterprom_fr/english/*.bytes; do
  result=$(strings "$f" | grep -i "Ah, Spooky" | head -3)
  if [ -n "$result" ]; then
    echo "=== $(basename $f) ==="
    echo "$result"
  fi
done