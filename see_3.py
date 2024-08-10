f=open('see_3.txt','w')
line=['line 1','line 2','line 3']
for l in line:
    f.write(l+'\\n'+'\n')
    # f.writelines(l+r'\n'+'\n')
    # f.write(l+repr('\n')+'\n')
f.close()