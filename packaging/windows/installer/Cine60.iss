; Cine60 installer (fork of Refrata, LucsLabs Studios)
; Built by tools/build.py:  ISCC /DAppVersion=x.y.z /DRoot=<repo> packaging\windows\installer\Cine60.iss
#ifndef AppVersion
  #define AppVersion "0.0.0"
#endif
#ifndef Root
  #define Root "..\..\.."
#endif
#define AppName "Cine60"
#define AppExe "Cine60.exe"
#define Studio "Cine60 (fork do Refrata, de LucsLabs Studios)"
#define ProgId "Cine60.Media"
#define CapKey "Software\Cine60\Capabilities"

[Setup]
AppId={{13DF4AA1-D826-4831-9D5A-F16C9B5821EB}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName} {#AppVersion}
AppPublisher={#Studio}
AppPublisherURL=https://github.com/adrianobbarcelos/Cine60
AppSupportURL=https://github.com/adrianobbarcelos/Cine60/issues
AppCopyright=© {#Studio}
VersionInfoCompany={#Studio}
VersionInfoDescription={#AppName} — instalador
VersionInfoVersion={#AppVersion}
DefaultDirName={autopf}\{#AppName}
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
OutputDir={#Root}\dist
OutputBaseFilename=Cine60-Setup-{#AppVersion}
SetupIconFile={#Root}\src\refrata\resources\icon.ico
UninstallDisplayIcon={app}\{#AppExe}
UninstallDisplayName={#AppName}
WizardStyle=modern
ShowLanguageDialog=auto
LanguageDetectionMethod=uilanguage
WizardImageFile={#Root}\packaging\windows\installer\art\wizard.bmp,{#Root}\packaging\windows\installer\art\wizard@2.5x.bmp
WizardSmallImageFile={#Root}\packaging\windows\installer\art\small.bmp,{#Root}\packaging\windows\installer\art\small@2.5x.bmp
Compression=lzma2/max
SolidCompression=yes
; the same compression on several cores (lzma2 in blocks, in a process of its own): faster builds
LZMAUseSeparateProcess=yes
LZMANumBlockThreads=6
ChangesAssociations=yes
; the same file times in every time zone (libVLC checks its plugins against plugins.dat)
TimeStampsInUTC=yes
CloseApplications=yes
; Only ask Restart Manager about executables: by default it registers every .exe/.dll that will be
; replaced (536 files with libVLC's plugins), and RmGetList took ~3.5 s on "Preparando para
; instalar". A running Cine60.exe is what holds those DLLs, so it is still found and closed.
CloseApplicationsFilter=*.exe
#ifdef Sign
; defined by tools/build.py (ISCC /DSign /Sbvsign=...): signs the setup and the uninstaller
SignTool=bvsign
SignedUninstaller=yes
#endif
RestartApplications=no
LicenseFile={#Root}\packaging\windows\installer\LICENSE-pt.txt

[Languages]
; follows the Windows display language (English when Inno has no translation, e.g. Chinese, Hindi)
Name: "en"; MessagesFile: "compiler:Default.isl"
Name: "ptbr"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"
Name: "es"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "fr"; MessagesFile: "compiler:Languages\French.isl"
Name: "de"; MessagesFile: "compiler:Languages\German.isl"
Name: "it"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "ru"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "pl"; MessagesFile: "compiler:Languages\Polish.isl"
Name: "tr"; MessagesFile: "compiler:Languages\Turkish.isl"
Name: "ja"; MessagesFile: "compiler:Languages\Japanese.isl"
Name: "ko"; MessagesFile: "compiler:Languages\Korean.isl"

[CustomMessages]
en.AssocTask=Show Cine60 in "Open with" for videos, music and playlists
en.LaunchNow=Open Cine60 now
en.WinIntegration=Windows integration:
en.ShortcutComment=Media player by {#Studio}
en.ProgIdName=Cine60 media
ptbr.AssocTask=Mostrar o Cine60 em "Abrir com" para vídeos, músicas e playlists
ptbr.LaunchNow=Abrir o Cine60 agora
ptbr.WinIntegration=Integração com o Windows:
ptbr.ShortcutComment=Player de mídia da {#Studio}
ptbr.ProgIdName=Mídia do Cine60
es.AssocTask=Mostrar Cine60 en "Abrir con" para vídeos, música y listas
es.LaunchNow=Abrir Cine60 ahora
es.WinIntegration=Integración con Windows:
es.ShortcutComment=Reproductor multimedia de {#Studio}
es.ProgIdName=Multimedia de Cine60
fr.AssocTask=Proposer Cine60 dans « Ouvrir avec » pour les vidéos, la musique et les playlists
fr.LaunchNow=Ouvrir Cine60 maintenant
fr.WinIntegration=Intégration à Windows :
fr.ShortcutComment=Lecteur multimédia de {#Studio}
fr.ProgIdName=Média Cine60
de.AssocTask=Cine60 unter „Öffnen mit“ für Videos, Musik und Playlists anzeigen
de.LaunchNow=Cine60 jetzt öffnen
de.WinIntegration=Windows-Integration:
de.ShortcutComment=Mediaplayer von {#Studio}
de.ProgIdName=Cine60-Medien
it.AssocTask=Mostra Cine60 in «Apri con» per video, musica e playlist
it.LaunchNow=Apri Cine60 ora
it.WinIntegration=Integrazione con Windows:
it.ShortcutComment=Lettore multimediale di {#Studio}
it.ProgIdName=Contenuto multimediale Cine60
ru.AssocTask=Показывать Cine60 в меню «Открыть с помощью» для видео, музыки и плейлистов
ru.LaunchNow=Открыть Cine60
ru.WinIntegration=Интеграция с Windows:
ru.ShortcutComment=Медиаплеер от {#Studio}
ru.ProgIdName=Медиафайл Cine60
pl.AssocTask=Pokazuj Cine60 w menu „Otwórz za pomocą” dla filmów, muzyki i playlist
pl.LaunchNow=Otwórz Cine60 teraz
pl.WinIntegration=Integracja z Windows:
pl.ShortcutComment=Odtwarzacz multimediów od {#Studio}
pl.ProgIdName=Multimedia Cine60
tr.AssocTask=Videolar, müzik ve çalma listeleri için "Birlikte aç" menüsünde Cine60'yı göster
tr.LaunchNow=Cine60'yı şimdi aç
tr.WinIntegration=Windows tümleştirmesi:
tr.ShortcutComment={#Studio} medya oynatıcısı
tr.ProgIdName=Cine60 medyası
ja.AssocTask=動画、音楽、プレイリストの「プログラムから開く」に Cine60 を表示する
ja.LaunchNow=Cine60 を今すぐ開く
ja.WinIntegration=Windows との統合:
ja.ShortcutComment={#Studio} のメディアプレーヤー
ja.ProgIdName=Cine60 メディア
ko.AssocTask=동영상, 음악, 재생 목록의 '연결 프로그램'에 Cine60 표시
ko.LaunchNow=지금 Cine60 열기
ko.WinIntegration=Windows 통합:
ko.ShortcutComment={#Studio}의 미디어 플레이어
ko.ProgIdName=Cine60 미디어

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"
Name: "assoc"; Description: "{cm:AssocTask}"; GroupDescription: "{cm:WinIntegration}"

[Files]
Source: "{#Root}\dist\Cine60\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#AppName}"; Filename: "{app}\{#AppExe}"; Comment: "{cm:ShortcutComment}"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\{#AppExe}"; Tasks: desktopicon

[Registry]
; ProgID used for every media type
Root: HKA; Subkey: "Software\Classes\{#ProgId}"; ValueType: string; ValueData: "{cm:ProgIdName}"; Flags: uninsdeletekey; Tasks: assoc
Root: HKA; Subkey: "Software\Classes\{#ProgId}\DefaultIcon"; ValueType: string; ValueData: """{app}\{#AppExe}"",0"; Tasks: assoc
Root: HKA; Subkey: "Software\Classes\{#ProgId}\shell\open"; ValueType: string; ValueName: "FriendlyAppName"; ValueData: "{#AppName}"; Tasks: assoc
Root: HKA; Subkey: "Software\Classes\{#ProgId}\shell\open\command"; ValueType: string; ValueData: """{app}\{#AppExe}"" ""%1"""; Tasks: assoc
; "Abrir com" entry for the executable
Root: HKA; Subkey: "Software\Classes\Applications\{#AppExe}"; ValueType: string; ValueName: "FriendlyAppName"; ValueData: "{#AppName}"; Flags: uninsdeletekey; Tasks: assoc
Root: HKA; Subkey: "Software\Classes\Applications\{#AppExe}\shell\open\command"; ValueType: string; ValueData: """{app}\{#AppExe}"" ""%1"""; Tasks: assoc
; Default Apps (Settings › Apps › Apps padrão)
Root: HKA; Subkey: "Software\Cine60"; Flags: uninsdeletekeyifempty; Tasks: assoc
Root: HKA; Subkey: "Software\Cine60"; Flags: uninsdeletekeyifempty; Tasks: assoc
Root: HKA; Subkey: "{#CapKey}"; ValueType: string; ValueName: "ApplicationName"; ValueData: "{#AppName}"; Flags: uninsdeletekey; Tasks: assoc
Root: HKA; Subkey: "{#CapKey}"; ValueType: string; ValueName: "ApplicationDescription"; ValueData: "Player moderno sobre o motor do VLC, da {#Studio}"; Tasks: assoc
Root: HKA; Subkey: "{#CapKey}"; ValueType: string; ValueName: "ApplicationIcon"; ValueData: """{app}\{#AppExe}"",0"; Tasks: assoc
Root: HKA; Subkey: "Software\RegisteredApplications"; ValueType: string; ValueName: "{#AppName}"; ValueData: "{#CapKey}"; Flags: uninsdeletevalue; Tasks: assoc
; "Iniciar com o Windows" is written by the app itself; never leave it behind after uninstalling
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: none; ValueName: "Cine60"; Flags: uninsdeletevalue
; per-extension entries (generated from refrata/media.py)
#include AddBackslash(Root) + "build\assoc.iss"

[Run]
Filename: "{app}\{#AppExe}"; Description: "{cm:LaunchNow}"; Flags: nowait postinstall skipifsilent
; in-app updates run the setup with /VERYSILENT /relaunch=1: start the new version afterwards
Filename: "{app}\{#AppExe}"; Flags: nowait; Check: RelaunchAfterUpdate

[Code]
function RelaunchAfterUpdate: Boolean;
begin
  Result := WizardSilent and (ExpandConstant('{param:relaunch|0}') = '1');
end;

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
