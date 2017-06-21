import pypandoc
import subprocess

if __name__ == '__main__':
    #output = pypandoc.convert_file('introduction.md', to='dzslides', outputfile="introduction.html")
    subprocess.run(['/Users/csaintje/bin/anaconda3/bin/pandoc', '-s', 'introduction.md',
                    '-t', 'dzslides', '-o', 'introduction.html',
                    '-i', '--self-contained'])
    output = pypandoc.convert_file('introduction.md', to='beamer', outputfile="introduction.pdf")
    assert output == ""

