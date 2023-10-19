# whats_a;pp_pdf_sending
arguments are below
python send.py -m "Here is your pdf."^
                -pdf "file.pdf" ^
                -sleep 15 ^
                -excel "numbers.xlsx"^
                -try 3
it will load numbers from excel from very first column
send pdf to all the numbers
if failed it will retry 3 time after some time
if any number failed even after sending 3 times, it will write those numbers in text file
