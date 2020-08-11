/** build.js
 * Build information for windows application installer
 */

var electronInstaller = require('electron-winstaller');

var settings = {
    appDirectory: './release-builds/venmo-automation-desktop-win32-ia32',
    outputDirectory: './installers',
    authors: 'mxchen',
    exe: './venmo-automation-desktop.exe'
};

resultPromise = electronInstaller.createWindowsInstaller(settings);
 
resultPromise.then(() => {
    console.log("Installer successfully created");
}, (e) => {
    console.log("Error creating the installer: ${e.message}")
});
