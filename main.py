import customtkinter
import db_connect

#test
import search_algorithm as greedy
import city as city

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("840x600")
        self.title("BeamMaps")
        self.minsize(840, 600)

        # create 2x2 grid system
        self.grid_rowconfigure((0), weight=0)
        self.grid_rowconfigure((1), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.db = db_connect.DBConnect()

        self.routeTxt = ""
        self.startingTxt = ""
        self.destinyTxt = ""
        self.routeTxt = ""
        self.selectedStart = -1
        self.selectedDestiny = -1

        self.routes = [[0, 19],
                       [0, 15],
                       [0, 16],
                       [1, 6],
                       [1, 17],
                       [1, 13],
                       [1, 5],
                       [2, 3],
                       [2, 14],
                       [2, 13],
                       [3, 10],
                       [4, 7],
                       [5, 15],
                       [7, 17],
                       [8, 11],
                       [8, 18],
                       [9, 10],
                       [9, 16],
                       [12, 15],
                       [12, 19],
                       [13, 14],
                       [14, 15],
                       [17, 18],
                       [18, 14]]

        # add frame to app

        #main frame
        self.titleFrame  = customtkinter.CTkFrame(self, height=100)
        self.titleFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")


        self.mainFrame  = customtkinter.CTkFrame(self)
        self.mainFrame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # side frame
        self.sideFrame  = customtkinter.CTkFrame(self)
        self.sideFrame.grid(row=0, column=3, rowspan=2, columnspan=1, padx=10, pady=10, sticky="nsew")
        self.sideFrame.rowconfigure(0, weight=0)
        self.sideFrame.rowconfigure(1, weight=1)
        self.sideFrame.rowconfigure(2, weight=0)
        self.sideFrame.rowconfigure(3, weight=0)

        # add widgets to app

    #Side Frame Widgets
        customtkinter.CTkLabel(self.sideFrame, text="Route", font=("YU Gothic UI Semibold", 28)).grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.routeTextBox = customtkinter.CTkTextbox(self.sideFrame, state=customtkinter.DISABLED, fg_color="#2B2B2B", font=("YU Gothic UI Semibold", 16))
        self.routeTextBox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.routeTextBox.tag_config("center", justify="center")

        self.totalDistanceLabel = customtkinter.CTkLabel(self.sideFrame, text="Total\n...", font=("YU Gothic UI Semibold", 28))
        self.totalDistanceLabel.grid(row=2, column=0, padx=15, pady=10, sticky="nsew")
        # self.updateRouteText()

        self.calculateRouteBtn = customtkinter.CTkButton(self.sideFrame, text="Calculate Route", fg_color="#083464", font=("YU Gothic UI Semibold", 16), command=self.calculateRoute, height=50)
        self.calculateRouteBtn.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

    #Title Frame Widgets
        self.chosenCityLabel = customtkinter.CTkLabel(self, text="Choose a city...", font=("YU Gothic UI Semibold", 28))
        self.chosenCityLabel.grid(row=0, column=0, columnspan=2, padx=20)

    #Main Frame Widgets
        
        customtkinter.CTkLabel(self.mainFrame, text="Remnant State", font=("YU Gothic UI Semibold", 32), text_color="#FFFFFF").pack(pady=10)

        #canva
        self.canvas = customtkinter.CTkCanvas(self.mainFrame, width=580, height=380, bg='#2B2B2B', highlightthickness=0)

        #add city button

        self.btns = []

        self.btns.append(self.canvas.create_oval(39, 110, 59, 130))     #0 Arad
        self.btns.append(self.canvas.create_oval(369, 289, 389, 309))   #1 Bucharest
        self.btns.append(self.canvas.create_oval(211, 332, 231, 352))   #2 Craiova
        self.btns.append(self.canvas.create_oval(117, 321, 137, 342))   #3 Dobreta
        self.btns.append(self.canvas.create_oval(542, 326, 562, 346))   #4 Eforie
        self.btns.append(self.canvas.create_oval(268, 157, 288, 177))   #5 Fagaras
        self.btns.append(self.canvas.create_oval(341, 350, 361, 370))   #6 Giurgiu
        self.btns.append(self.canvas.create_oval(511, 266, 531, 286))   #7 Hirsova
        self.btns.append(self.canvas.create_oval(446, 94, 466, 114))    #8 Iasi
        self.btns.append(self.canvas.create_oval(117, 233, 137, 253))   #9 Lugoj
        self.btns.append(self.canvas.create_oval(120, 278, 140, 298))   #10 Mehadia
        self.btns.append(self.canvas.create_oval(374, 61, 394, 81))     #11 Neamf
        self.btns.append(self.canvas.create_oval(81, 24, 101, 44))      #12 Oradea
        self.btns.append(self.canvas.create_oval(285, 247, 305, 267))   #13 Pitesti
        self.btns.append(self.canvas.create_oval(191, 199, 211, 219))   #14 Rimnicu Vikea
        self.btns.append(self.canvas.create_oval(164, 147, 184, 167))   #15 Sibiu
        self.btns.append(self.canvas.create_oval(41, 199, 61, 219))     #16 Timisoara
        self.btns.append(self.canvas.create_oval(430, 263, 450, 283))   #17 Urziceni
        self.btns.append(self.canvas.create_oval(484, 161, 504, 181))   #18 Urziceni
        self.btns.append(self.canvas.create_oval(56, 67, 76, 87))       #19 Zerind

        # add road lines

        self.roads = []

        self.roads.append(self.canvas.create_line(39 + 10, 110 + 10, 56 + 10, 67 + 10)) 
        self.roads.append(self.canvas.create_line(39 + 10, 110 + 10, 164 + 10, 147 + 10))
        self.roads.append(self.canvas.create_line(39 + 10, 110 + 10, 41 + 10, 199 + 10))

        self.roads.append(self.canvas.create_line(369 + 10, 289 + 10, 341 + 10, 350 + 10))
        self.roads.append(self.canvas.create_line(369 + 10, 289 + 10, 430 + 10, 263 + 10))
        self.roads.append(self.canvas.create_line(369 + 10, 289 + 10, 285 + 10, 247 + 10))
        self.roads.append(self.canvas.create_line(369 + 10, 289 + 10, 268 + 10, 157 + 10))

        self.roads.append(self.canvas.create_line(211 + 10, 332 + 10, 117 + 10, 321 + 10))
        self.roads.append(self.canvas.create_line(211 + 10, 332 + 10, 191 + 10, 199 + 10))
        self.roads.append(self.canvas.create_line(211 + 10, 332 + 10, 285 + 10, 247 + 10))

        self.roads.append(self.canvas.create_line(117 + 10, 321 + 10, 120 + 10, 278 + 10))

        self.roads.append(self.canvas.create_line(542 + 10, 326 + 10, 511 + 10, 266 + 10))

        self.roads.append(self.canvas.create_line(268 + 10, 157 + 10, 164 + 10, 147 + 10))

        self.roads.append(self.canvas.create_line(511 + 10, 266 + 10, 430 + 10, 263 + 10))

        self.roads.append(self.canvas.create_line(446 + 10, 94 + 10, 374 + 10, 61 + 10))
        self.roads.append(self.canvas.create_line(446 + 10, 94 + 10, 484 + 10, 161 + 10))

        self.roads.append(self.canvas.create_line(117 + 10, 233 + 10, 120 + 10, 278 + 10))
        self.roads.append(self.canvas.create_line(117 + 10, 233 + 10, 41 + 10, 199 + 10))

        self.roads.append(self.canvas.create_line(81 + 10, 24 + 10, 164 + 10, 147 + 10))
        self.roads.append(self.canvas.create_line(81 + 10, 24 + 10, 56 + 10, 67 + 10))

        self.roads.append(self.canvas.create_line(285 + 10, 247 + 10, 191 + 10, 199 + 10))

        self.roads.append(self.canvas.create_line(191 + 10, 199 + 10, 164 + 10, 147 + 10))

        self.roads.append(self.canvas.create_line(430 + 10, 263 + 10, 484 + 10, 161 + 10))

        # add road distance

        roadDists = []

        roadDists.append(75)
        roadDists.append(140)
        roadDists.append(118)

        roadDists.append(90)
        roadDists.append(85)
        roadDists.append(101)
        roadDists.append(211)

        roadDists.append(120)
        roadDists.append(145)
        roadDists.append(138)

        roadDists.append(75)

        roadDists.append(86)

        roadDists.append(99)

        roadDists.append(98)

        roadDists.append(87)
        roadDists.append(92)
        
        roadDists.append(70)
        roadDists.append(111)

        roadDists.append(151)
        roadDists.append(71)

        roadDists.append(97)

        roadDists.append(80)

        roadDists.append(142)

        roadDists.append(142)
       

        # TxtX = self.canvas.bbox(self.roads[0])[2]
        # TxtY = self.canvas.bbox(self.roads[0])[3]

        for roadIndex in range(len(self.roads)):
            TxtX = self.canvas.bbox(self.roads[roadIndex])[0] + ((self.canvas.bbox(self.roads[roadIndex])[2] - self.canvas.bbox(self.roads[roadIndex])[0])/2)
            TxtY = self.canvas.bbox(self.roads[roadIndex])[1] + ((self.canvas.bbox(self.roads[roadIndex])[3] - self.canvas.bbox(self.roads[roadIndex])[1])/2)

            self.canvas.create_text(TxtX, TxtY, text=str(roadDists[roadIndex])+"km", fill="#2B2B2B", font=("Segoe UI Black", 10))

        for roadIndex in range(len(self.roads)):
            TxtX = self.canvas.bbox(self.roads[roadIndex])[0] + ((self.canvas.bbox(self.roads[roadIndex])[2] - self.canvas.bbox(self.roads[roadIndex])[0])/2)
            TxtY = self.canvas.bbox(self.roads[roadIndex])[1] + ((self.canvas.bbox(self.roads[roadIndex])[3] - self.canvas.bbox(self.roads[roadIndex])[1])/2)
            
            self.canvas.create_text(TxtX, TxtY, text=str(roadDists[roadIndex])+"km", fill="white", font=("Segoe UI", 10))

        # add city name labels

        self.canvas.create_text(64 - 0, 9 - 0, text="Oradea", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(79 - 0, 78 - 0, text="Zerind", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(11 - 8, 111 + 8, text="Arad", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(19 - 20, 221 + 8, text="Timissoara", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(112 - 8, 213 + 2, text="Lugoj", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(177 - 18, 134 + 2, text="Sibiu", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(255 - 5, 140 + 5, text="Fagaras", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(207 - 5, 187 + 5, text="Rimnicu Viicea", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(276 - 8, 231 + 5, text="Pitesti", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(141 + 2, 277 + 10, text="Mehadia", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(103 - 5, 340 + 10, text="Dobreta", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(201 - 5, 352 + 10, text="Craiova", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(363 + 3, 352 + 10, text="Giurgiu", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(379 + 3, 309 + 10, text="Bucharest", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(417 - 30, 309 - 60, text="Urziceni", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(501 - 5, 248 + 5, text="Hirsova", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(534 - 0, 350 + 5, text="Eforie", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(506 + 2, 164 + 7, text="Vaslui", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(470 - 0, 96 + 7, text="iasi", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")
        self.canvas.create_text(364 - 4, 42 + 7, text="Neamt", font=("YU Gothic UI Semibold", 11), anchor="w", fill="#FFFFFF")

        self.canvas.pack(pady=(10 , 0))
        index = 1
        for btn in self.btns:
            self.canvas.itemconfigure(index, fill="#F4F4F4")
            self.canvas.itemconfigure(index, outline="#000000")
            self.canvas.itemconfigure(index, width=2)
            self.canvas.tag_raise(index)
            
            self.canvas.tag_bind(btn, "<Button-1>", self.clicked)
            index+=1
        
        self.clearRoads()

    # add methods to app
        self.test = 0

    def clearRoads(self):
        index = len(self.btns)+1
        for road in self.roads:
            self.canvas.itemconfigure(index, fill="#A3A3A3")
            self.canvas.itemconfigure(index, width=4)
            self.canvas.tag_lower(index)
            index+=1

    def calculateRoute(self):
        if(self.selectedStart != -1 and self.selectedDestiny != -1):
            self.greedy = greedy.Greedy(self.selectedDestiny)
            self.greedy.search(city.city(self.selectedStart, 'Arad'))
            self.routeTxt = self.greedy.resultTxt
            self.test+=1

            self.updateRouteText(str(self.greedy.resultDist))
            # self.canvas.itemconfigure(len(self.btns)+1, width=6, fill="#10A674")

            roadIndex = 0
            print(str(self.greedy.roadPath0)+" | "+str(self.greedy.roadPath1))
            self.clearRoads()
            for x in range(len(self.greedy.roadPath0)):
                routeIndex = 0
                # print(str(self.routes[0][0])+", "+str(self.routes[0][1])+" | "+str(self.greedy.roadPath0[0])+", "+str(self.greedy.roadPath0[1]))
                for route in self.routes:
                    routeIndex += 1
                    if(route[0] == self.greedy.roadPath0[roadIndex] and route[1] == self.greedy.roadPath1[roadIndex]):
                        self.canvas.itemconfigure(len(self.btns)+routeIndex, width=6, fill="#10A674")
                        print("painted")
                    if(route[1] == self.greedy.roadPath0[roadIndex] and route[0] == self.greedy.roadPath1[roadIndex]):
                        print("painted")
                        self.canvas.itemconfigure(len(self.btns)+routeIndex, width=6, fill="#10A674")
                roadIndex += 1
        else:
            self.routeTxt = ""
            self.updateRouteText(0)
            self.clearRoads()


    def updateRouteText(self, _routeTotalDist):
        # self.routeTxt = _routeTxt
        self.routeTextBox.configure(state=customtkinter.NORMAL)
        self.routeTextBox.delete(1.0, customtkinter.END)
        self.routeTextBox.insert(1.0, self.routeTxt)
        self.routeTextBox.configure(state=customtkinter.DISABLED)
        self.routeTextBox.tag_add("center", 1.0, customtkinter.END)

        self.totalDistanceLabel.configure(text="Total\n"+str(_routeTotalDist)+"km")

    def updateCityLabel(self):
        if(self.selectedStart == -1): self.startingTxt = "Choose an Origin"
        else: self.startingTxt = self.db.GetCityName(self.selectedStart)
        if(self.selectedDestiny == -1): self.destinyTxt = "Choose a Destiny"
        else: self.destinyTxt = self.db.GetCityName(self.selectedDestiny)
        self.chosenCityLabel.configure(text=self.startingTxt+" -> "+self.destinyTxt)

    def paintCity(self):
        index = 1
        for btn in self.btns:
            self.canvas.itemconfigure(index, fill="#F4F4F4")
            self.canvas.itemconfigure(index, outline="#000000")
            self.canvas.itemconfigure(index, width=2)
            index+=1
        if(self.selectedStart != -1):
            self.canvas.itemconfigure(self.selectedStart+1, fill="blue")
            self.canvas.itemconfigure(self.selectedStart+1, width=1)
        if(self.selectedDestiny != -1):
            self.canvas.itemconfigure(self.selectedDestiny+1, fill="green")
            self.canvas.itemconfigure(self.selectedDestiny+1, width=1)
        self.updateCityLabel()

    def clicked(self, event):
        item = event.widget.find_closest(event.x, event.y)
        if(self.canvas.itemcget(item, "fill") != "#A3A3A3" and self.canvas.itemcget(item, "fill") != "#FFFFFF"):
            if(self.selectedStart == -1 or self.selectedDestiny == -1):
                if(self.selectedStart == -1 and self.selectedDestiny != item[0]-1): self.selectedStart = item[0]-1
                elif (self.selectedStart == -1 and self.selectedDestiny == item[0]-1): self.selectedDestiny = -1
                elif(self.selectedDestiny == -1 and self.selectedStart != item[0]-1): self.selectedDestiny = item[0]-1
                elif (self.selectedDestiny == -1 and self.selectedStart == item[0]-1): self.selectedStart = -1
                print("Clicked "+str(item[0]))
            else:
                if (self.selectedStart == item[0]-1):
                    self.selectedStart = -1
                if (self.selectedDestiny == item[0]-1):
                    self.selectedDestiny = -1
            self.paintCity()
        else:
            print("Clicked on a line, woof, saved you, you're welcome :)")



app = App()
app.mainloop()