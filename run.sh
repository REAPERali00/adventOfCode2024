function m() {
  python3 main.py &>output.txt
  cat output.txt
}
function t() {
  python3 test.py &>output.txt
  cat output.txt
}

m
