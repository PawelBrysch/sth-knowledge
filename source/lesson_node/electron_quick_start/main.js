// Modules to control application life and create native browser window
const {app, BrowserWindow} = require('electron');
const path = require('path');

//TODO jak dziala GC w js
let mainWindow;

function createWindow () {
  mainWindow = new BrowserWindow({width: 800, height: 600, webPreferences: {preload: path.join(__dirname, 'preload.js')}});
  mainWindow.loadFile('index.html');

  /** Open the DevTools.*/
  mainWindow.webContents.openDevTools();

  // Niby
  mainWindow.on('closed', function () {mainWindow = null})
}

app.on('ready', createWindow);


// Quit when all windows are closed.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
});

app.on('activate', function () {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) createWindow()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
