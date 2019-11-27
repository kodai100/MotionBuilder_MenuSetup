import sys
import os
import traceback
import glob

from pyfbsdk import *
from pyfbsdk_additions import *

class MenuCreator():
	
	def __init__(self, toolName, toolFolderName):
		
		self.toolName = toolName

		self.basePath = os.path.dirname(os.path.abspath(self.currentPath()))
		self.toolRootPath = self.basePath + "\\Scripts\\" + toolFolderName

		self.contentFolderPath = self.GetContentFolderPath()

		mainMenu = FBMenuManager()
		_menuItem = mainMenu.InsertAfter(None, "PythonTools", toolName)
		menuRoot = mainMenu.GetMenu(toolName)

		self.scriptGrp = {}
		self.addMenu(menuRoot, self.contentFolderPath, self.scriptGrp)

	def currentPath(self):
		curpath = os.path.dirname(traceback.extract_stack()[-1][0])
		return curpath

	def GetContentFolderPath(self):
		pathList = []

		for folder in os.listdir(self.toolRootPath):
		
			path = os.path.join(self.toolRootPath, folder)
		
			if os.path.isdir(path):
			
				pathList.append(path)

				if (path) not in sys.path:
					sys.path.append(path)

		return pathList

	def eventMenu(self, control, event):
		scripts = self.scriptGrp[event.Name]
		FBApplication().ExecuteScript(scripts)

	def createButtonWithFolder(self, menuRoot, folderPathList, source, index):

		for folderPath in folderPathList:

			subMenu = FBGenericMenu()

			lists = glob.glob(folderPath+ "\\*.py")

			for file in lists:
				index += 1
				fileName = os.path.basename(file).strip(".py")
				subMenu.InsertLast(fileName, index)
				source[fileName] = file
			
			subMenu.OnMenuActivate.Add(self.eventMenu)
			
			subRootName = os.path.basename(folderPath)

			menuRoot.InsertLast(subRootName, 100 * (index + 1), subMenu)

		return index

	def createButton(self, menuRoot, scriptFolderPath, source, index):

		lists = glob.glob(scriptFolderPath + "\\*.py")
			
		for file in lists:
			index += 1
			name = os.path.basename(file).strip(".py")
			menuRoot.InsertLast(name, index + 1)
			source[name] = (self.toolRootPath + "\\" + name  + ".py")
		
		menuRoot.OnMenuActivate.Add(self.eventMenu)

		return index

	def addMenu(self, menuRoot, folderPathList, source):
		
		index = 0
		index = self.createButtonWithFolder(menuRoot, folderPathList, source, index)
		index = self.createButton(menuRoot, self.toolRootPath, source, index)