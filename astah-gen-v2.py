# -*- coding: utf-8 -*-
import io
import os, sys

def genclass():
    # Open a file
    path = os.getcwd()
    dirs = os.listdir(path)
    
    for file in dirs:
        
        newline = ''
        htmlBody = ''
        erasetext = False
        
        if file.startswith("alldiagrams"):
            #Reding html file
            basefile = open(file, 'r')
            htmlBody = basefile.read()
            
            #REP1
            htmlBody = htmlBody.replace('<LINK REL ="stylesheet" TYPE="text/css" HREF="stylesheet.css" TITLE="Style">',' ')
            
            strAux1 = "\n".join(['<FONT size="+1" CLASS="FrameHeadingFont">', '<B>All Diagrams</B></FONT>', '<BR>' ])
            htmlBody = htmlBody.replace(strAux1,' ')
            
            
            #REP2
            strAuxLongLine = '<td style="background-color: rgb(217, 217, 217); width: 521px; text-align: center;"><b style=""><span style="font-size: 12pt; font-family: &quot;Segoe UI&quot;,&quot;sans-serif&quot;; color: rgb(102, 102, 102);">Todas os Diagramas</span></b><span style="font-size: 12pt; font-family: &quot;Segoe UI&quot;,&quot;sans-serif&quot;; color: rgb(102, 102, 102);"></span></td>'
            strAux1 = "\n".join(['<TABLE BORDER="0" WIDTH="100%" >', '<tr>',strAuxLongLine, '</tr>' ])
            htmlBody = htmlBody.replace('<TABLE BORDER="0" WIDTH="100%" SUMMARY="">', strAux1)
            
            #REP3
            htmlBody = htmlBody.replace('title="class in "','style=" text-decoration:none; font-size: 12pt; font-family: &quot;Segoe UI&quot;,&quot;sans-serif&quot;; color: rgb(102, 102, 102);"')
            
            
            basefile.close()
            #Saving
            arq = open(file, 'w') 
            arq.write(htmlBody) 
            arq.close() 
            continue
        if file.startswith("br.gov.rj.rio"):
            continue
        if file.startswith("allclasses"):
            #Reding html file
            basefile = open(file, 'r')
            htmlBody = basefile.read()
            
            #REP1
            htmlBody = htmlBody.replace('<LINK REL ="stylesheet" TYPE="text/css" HREF="stylesheet.css" TITLE="Style">',' ')
            
            strAux1 = "\n".join(['<FONT size="+1" CLASS="FrameHeadingFont">', '<B>All Classes</B></FONT>', '<BR>' ])
            htmlBody = htmlBody.replace(strAux1,' ')
            
            
            #REP2
            strAuxLongLine = '<td style="background-color: rgb(217, 217, 217); width: 521px; text-align: center;"><b style=""><span style="font-size: 12pt; font-family: &quot;Segoe UI&quot;,&quot;sans-serif&quot;; color: rgb(102, 102, 102);">Todas as Classes</span></b><span style="font-size: 12pt; font-family: &quot;Segoe UI&quot;,&quot;sans-serif&quot;; color: rgb(102, 102, 102);"></span></td>'
            strAux1 = "\n".join(['<TABLE BORDER="0" WIDTH="100%" >', '<tr>',strAuxLongLine, '</tr>' ])
            htmlBody = htmlBody.replace('<TABLE BORDER="0" WIDTH="100%" SUMMARY="">', strAux1)
            
            #REP3
            htmlBody = htmlBody.replace('title="class in &lt;Unnamed&gt;"','style=" text-decoration:none; font-size: 12pt; font-family: &quot;Segoe UI&quot;,&quot;sans-serif&quot;; color: rgb(102, 102, 102);"')
            
            
            basefile.close()
            #Saving
            arq = open(file, 'w') 
            arq.write(htmlBody) 
            arq.close() 
            continue
        if file.startswith("deprecated-list"):
            continue
        if file.startswith("help-doc"):
            continue
            
        if file.startswith("index"):
            #Reding html file
            basefile = open(file, 'r')
            htmlBody = basefile.read()
            htmlBody = htmlBody.replace('<FRAME ','<FRAME frameborder="0"')
            basefile.close()
            #Saving
            arq = open(file, 'w') 
            arq.write(htmlBody) 
            arq.close() 
            continue
            
        if file.startswith("overview-tree"):
            continue
        if file.startswith("package"):
            continue
        if file.startswith("stylesheet"):
            continue
        if file.startswith("uml-"):
            continue
        if file.startswith("constant-values"):
            continue
        if file.startswith("images"):
            continue
        if file.startswith("resources"):
            continue

        if file.endswith(".py"):
            continue

        if not file.endswith(".html"):
            continue            

        
        #Reding html file
        basefile = open(file, 'r') 
        
        
        
        for line in basefile:
            newline = line
            if newline.strip() == '<LINK REL ="stylesheet" TYPE="text/css" HREF="stylesheet.css" TITLE="Style">':
                #newline = ''
                erasetext = True
                
            #if newline.strip() == '</HEAD>':
                #erasetext = False
                
            
            #if newline.strip() == '<SCRIPT type="text/javascript">':
             #       erasetext = True

            #if newline.strip() == '</NOSCRIPT>':
             #       erasetext = False

                    

            
            #if newline.strip() == '<!-- ========= START OF TOP NAVBAR ======= -->':
                    #erasetext = True
            
            if newline.strip() == '<!-- ========= END OF TOP NAVBAR ========= -->':
                erasetext = False
                
            if newline.strip() == '<!-- ======= START OF BOTTOM NAVBAR ====== -->':
                erasetext = True
                
            if newline.strip() == '<!-- ======== END OF BOTTOM NAVBAR ======= -->':
                erasetext = False
                
            if erasetext == True:
                newline = ''
            
            htmlBody = htmlBody + newline
        
        strAux2 = '<H2 style=" text-align:center; font-size: 18pt; font-family: &quot;Segoe UI&quot;,&quot;sans-serif&quot;; color: rgb(102, 102, 102);">Classe: '
        
        strAux1 = "\n".join(['<H2>', 'Class '])
                
        htmlBody = htmlBody.replace(strAux1 ,strAux2)
        
        htmlBody = htmlBody.replace('TABLE BORDER="1"' ,'TABLE BORDER="0"')
        
        htmlBody = htmlBody.replace('<TR BGCOLOR="#CCCCFF" CLASS="TableHeadingColor">' , '<TR BGCOLOR="#D9D9D9">')
            
        htmlBody = htmlBody.replace('<B>Field Summary</B>' , '<B>Resumo do Campo</B>')
        
        htmlBody = htmlBody.replace('<B>Method Summary</B>' , '<B>Resumo do Método</B></FONT></TH>')
        
        htmlBody = htmlBody.replace('<B>Field Detail</B>' ,'<B>Detalhes do Campo</B>')
        
        htmlBody = htmlBody.replace('<B>Method Detail</B>' ,'<B>Detalhes do Método</B>')
        
        htmlBody = htmlBody.replace('SIZE="+2"' ,'SIZE="+2" style="font-family: &quot;Segoe UI&quot;,&quot;sans-serif&quot;; color: rgb(102, 102, 102);"')
        
        
        #htmlBody = basefile.read() 
        
        basefile.close()
        
        
        arq = open(file, 'w') 
        arq.write(htmlBody) 
        arq.close() 



genclass()
print "Done!"
myBody = ""
        
#myBody = myBody + swallow(path + '/'  + file);