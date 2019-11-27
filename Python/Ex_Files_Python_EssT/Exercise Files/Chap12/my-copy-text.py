def main():
    infile = open('lines.txt', 'rt')
    outfile = open('mylines-copy.txt', 'wt')
    for line in infile:
        outfile.writelines(line) # or writelines()
        print('.', end='', flush=True)
    outfile.close()
    infile.close()
    print('\ndone.')

if __name__ == '__main__': main()