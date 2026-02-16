{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Bold;\f1\froman\fcharset0 Times-Roman;\f2\fmodern\fcharset0 Courier;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat0\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat0\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid101\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat0\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid201\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid3}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sa321\partightenfactor0

\f0\b\fs26 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 GOOD PERFORMANCE TIME APP - Anas MM \
Uninformed Search Visualization in a Dynamic Grid Environment
\fs36 \

\f1\b0\fs24 This project is an AI Pathfinder that demonstrates how different uninformed (blind) search algorithms explore a grid.\uc0\u8232 It visually shows how each algorithm \'93thinks\'94 step-by-step while navigating from a Start point (S) to a Target point (T), avoiding both static and dynamic obstacles.\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 Unlike traditional static pathfinding demos, this system includes 
\f0\b dynamic hurdles
\f1\b0  that may randomly appear while the agent is moving. When that happens, the agent detects the blockage and automatically re-plans a new path.\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 Implemented Algorithms\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 The following uninformed search algorithms are implemented:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls1\ilvl0\cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Breadth-First Search (BFS)\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Depth-First Search (DFS)\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Uniform-Cost Search (UCS)\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Depth-Limited Search (DLS)\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Iterative Deepening DFS (IDDFS)\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Bidirectional Search\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 \strokec2 Each algorithm follows a strict clockwise movement order including all diagonals.\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 Visualization Features\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 The GUI (built using Matplotlib) shows:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls2\ilvl0\cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Frontier nodes (nodes waiting to be explored)\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Explored nodes (already visited)\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Final path from Start to Target\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Real-time animation of the search process\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Dynamic obstacles appearing during execution\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Automatic re-planning when the path becomes blocked\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 \strokec2 Every GUI window is titled:\
GOOD PERFORMANCE TIME APP\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 Dependencies\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 This project uses:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0\cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Python 3\
\ls3\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 NumPy\
\ls3\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Matplotlib\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 \strokec2 All required packages are listed in 
\f2\fs26 \strokec2 requirements.txt
\f1\fs24 \strokec2 .\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 good-performance-time-app/\
\uc0\u9474 \
\uc0\u9500 \u9472 \u9472  requirements.txt\
\uc0\u9500 \u9472 \u9472  README.md\
\uc0\u9492 \u9472 \u9472  src/\
    \uc0\u9500 \u9472 \u9472  main.py\
    \uc0\u9500 \u9472 \u9472  grid.py\
    \uc0\u9500 \u9472 \u9472  visualizer.py\
    \uc0\u9492 \u9472 \u9472  search/\
        \uc0\u9500 \u9472 \u9472  bfs.py\
        \uc0\u9500 \u9472 \u9472  dfs.py\
        \uc0\u9500 \u9472 \u9472  ucs.py\
        \uc0\u9500 \u9472 \u9472  dls.py\
        \uc0\u9500 \u9472 \u9472  iddfs.py\
        \uc0\u9500 \u9472 \u9472  bidir.py\
        \uc0\u9492 \u9472 \u9472  common.py\
\
}