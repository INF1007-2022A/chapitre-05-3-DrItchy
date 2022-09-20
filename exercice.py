#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_num_letters(text):
    c=0
    for i in range(len(text)):
       if text[i].isalnum():
           c+=1
    return c

def get_word_length_histogram(text):
    l,c=[],0
    for i in range(len(text)):
        if text[i].isalnum() or text[i].isspace():
            c+=1
            if text[i].isspace():
                c-=1
                while len(l)-1<c:
                    l.append(0)
                l[c]+=1
                c=0
    while len(l)-1<c:
        l.append(0)
    l[c]+=1
    return l

def format_histogram(histogram):
    ROW_CHAR = "*"
    for i in range(len(histogram)):
        print(f"{i} {histogram[i]*ROW_CHAR}")

def format_horizontal_histogram(histogram):
    BLOCK_CHAR = "|"
    LINE_CHAR = "¯"
    m,l=max(histogram),""
    while m!=0:
        for i in range(1,len(histogram)):
            if histogram[i]>=m:
                l+=BLOCK_CHAR
            else:
                l+=" "
        print(l)
        l=""
        m-=1
    print(LINE_CHAR*(len(histogram)-1))


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
