# whats_a;pp_pdf_sending <br />
arguments are below <br />
python send.py -m "Here is your pdf."^ <br />
                &emsp;&emsp;&emsp;-pdf "file.pdf" ^ <br />
                &emsp;&emsp;&emsp;-sleep 15 ^ <br />
                &emsp;&emsp;&emsp;-excel "numbers.xlsx"^ <br />
                &emsp;&emsp;&emsp;-try 3 <br />
it will load numbers from Excel from very first column <br />
send pdf to all the numbers <br />
if failed it will retry 3 times after some time <br />
if any number fails even after sending 3 times, it will write those numbers in a text file <br />
