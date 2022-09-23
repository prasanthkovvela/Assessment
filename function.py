def UniqueAuthor(exact_data):
    authors_list=[]
    for i in exact_data:
        auth=i[1:]
        authors_list.extend(auth)
    return authors_list
    

def toFindNumberOfBooks(filtered_auth):
    noOfBooks=[]
    for i in filtered_auth:
        count=filtered_auth.count(i)
        string=str(i)+" = "+str(count)
        if string not in noOfBooks:
            noOfBooks.append(string)
    return noOfBooks

       
def toFindMaximumBooks(numberOfBooks):
    large=[] 
    for i in numberOfBooks:
        k=int(i[len(i)-1])
        large.append(i)
    l=max(large)    
    finalL=large.index(l)
    result=numberOfBooks[finalL]
    return result
        
def books(exact_data):
    year=[]
    for i in exact_data:
        if "(2012)" in i[0]:
            year.append(i[0])
    return year
 
 
 
        
input =open("books.txt","r")
file=input.readlines()
main=[]
for i in file:
    main.append(i[:-1].split(","))
exact_data=[]
for i in main:
    t=[]
    for j in i:
        if j[-1]==";":
            t.append(j[:-1].strip())
        else:
            t.append(j.strip())
    exact_data.append(t)
# print(exact_data)
# ----------------------------------------------------------------------------

filtered_auth=UniqueAuthor(exact_data)
numberOfBooks=toFindNumberOfBooks(filtered_auth)
MaximumBooks=toFindMaximumBooks(numberOfBooks)
booksIn2012=books(exact_data)

print(set(filtered_auth))
print(numberOfBooks)
print(MaximumBooks)
print(booksIn2012)
