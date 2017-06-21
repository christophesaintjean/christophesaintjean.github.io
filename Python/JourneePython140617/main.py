import pypandoc
import subprocess

if __name__ == '__main__':
    #output = pypandoc.convert_file('introduction.md', to='dzslides', outputfile="introduction.html")
    subprocess.run(['/Users/csaintje/bin/anaconda3/bin/pandoc', '-s', 'introduction.md',
                    '-t', 'dzslides', '-o', 'introduction.html',
                    '-i', '--self-contained'])
    #output = pypandoc.convert_file('introduction.md', to='beamer', outputfile="introduction.pdf")
    #assert output == ""

    # pandoc -t beamer -V theme:Varsaw -s expose.md -o expose.pdf

    # output = pypandoc.convert_file('expose.md', to='beamer', outputfile="expose.pdf",
    #                             extra_args=['-V', 'theme:Warsaw'])
    # output = pypandoc.convert_file('expose.md', to='latex', outputfile="expose2.tex")
    # subprocess.run(['pdflatex', 'expose2.tex'])
    # # pandoc -t beamer -V theme:TemplateMIA -s expose.md -o expose.pdf
    #output = pypandoc.convert_file('expose.md', to='beamer', outputfile="expose.pdf",
    #                               extra_args=['-V', 'theme:TemplateMIA'])
    #assert output == ""

