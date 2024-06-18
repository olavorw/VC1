[Setup]
AppName=VC1
AppVersion=v0.41-alpha
DefaultDirName={pf}\VC1
DefaultGroupName=VC1
OutputDir=.
OutputBaseFilename=VC1Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\olavs\OneDrive\Documents\Programming\voicechanger\releases\v0.42-alpha\VC1.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\olavs\OneDrive\Documents\Programming\voicechanger\releases\v0.42-alpha\CODE_OF_CONDUCT.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\olavs\OneDrive\Documents\Programming\voicechanger\releases\v0.42-alpha\EULA.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\olavs\OneDrive\Documents\Programming\voicechanger\releases\v0.42-alpha\LICENSE.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\olavs\OneDrive\Documents\Programming\voicechanger\releases\v0.42-alpha\README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\olavs\OneDrive\Documents\Programming\voicechanger\releases\v0.42-alpha\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\VC1"; Filename: "{app}\VC1.exe"
Name: "{group}\Uninstall VC1"; Filename: "{uninstallexe}"
