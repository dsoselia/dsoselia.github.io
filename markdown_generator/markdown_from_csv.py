# %%
import pandas as pd
import math
columns = "Authors,Title,Publication,Volume,Number,Pages,Year,Publisher".split(",")
publications = pd.read_csv('citations.csv', names=columns)

# sort by year
publications = publications.sort_values(by='Year', ascending=False)

my_names = ["D Soselia", "Davit Soselia", "D. S.", "Soselia D.", "Soselia Davit"]

def is_author(author):
    author = ''.join(e for e in author if e.isalnum())
    author = author.lower()
    for name in my_names:
        # remove all non-alphanumeric characters from the name
        name = ''.join(e for e in name if e.isalnum())
        name = name.lower()
        if name in author:
            return True
    return False

# %%

markdown_text = ""

for index, row in publications.iterrows():
    paper_text = ""
    authors = row['Authors'].split(';')
    author_text = ""
    for author in authors:
        author = author.strip()
        author = author.replace(",", " ")
        author = author.replace(";", " ")


        if is_author(author):
            author_text += f"**{author}**, "
        else:
            author_text += f"{author}, "
    
    author_text = author_text[:-4] # remove the last comma and space
    year = row['Year']
    title = row['Title']
    paper_text += f"{author_text} ({int(year)}). {title}."
    publication = row['Publication']
    if str(publication) != "nan":
        paper_text += f" {publication}."
    print(type(publication))
    volume = row['Volume']
    number = row['Number']
    pages = row['Pages']
    if str(volume) != "nan" and str(number) != "nan" and str(pages) != "nan":
        paper_text += f" {volume}({number}): {pages}."
    publisher = row['Publisher']
    if str(publisher) != "nan":
        paper_text += f" {publisher}."
    
    paper_text += '''

'''
    markdown_text += paper_text




with open('papers.md', 'w') as f:
    f.write(markdown_text)