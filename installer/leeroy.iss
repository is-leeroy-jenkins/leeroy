#define MyAppName "Leeroy"
#ifndef MyAppVersion
  #define MyAppVersion "0.1.0"
#endif

[Setup]
AppId={{EC0EABBD-05CA-4AA0-B783-206DC4CA06F6}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher=is-leeroy-jenkins
DefaultDirName={localappdata}\Programs\Leeroy
DefaultGroupName=Leeroy
OutputDir=..\dist-installer
OutputBaseFilename=Leeroy-Setup-{#MyAppVersion}
Compression=lzma2
SolidCompression=yes
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=lowest
WizardStyle=modern
UninstallDisplayName=Leeroy
UninstallDisplayIcon={app}\Leeroy.exe
CloseApplications=yes

[Files]
Source: "..\dist\Leeroy\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Icons]
Name: "{group}\Leeroy"; Filename: "{app}\Leeroy.exe"
Name: "{autodesktop}\Leeroy"; Filename: "{app}\Leeroy.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Leeroy.exe"; Description: "Launch Leeroy"; Flags: nowait postinstall skipifsilent
