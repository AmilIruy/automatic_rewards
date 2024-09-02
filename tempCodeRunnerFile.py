im2 = PhotoImage(file="imagens\Art_Print__Front_View_of_Human_Skeleton_in_Fighting_Stance_by_Stocktrek_Images___24x24in-removebg-preview.png")
im2 = im2.subsample(5,5)
figura2 = Label(janela, image=im2,bg="#111111")
figura2.grid(row=0, column=0, padx=(300, 0), pady=(280, 10), sticky="ne")

im3 = PhotoImage(file="imagens\direita esqueleto.png") 
im3 = im3.subsample(5,5)
figura3 = Label(janela, image=im3,bg="#111111")
figura3.grid(row=0, column=0, padx=(153, 150), pady=(120, 10), sticky="w")