import wmi

c = wmi.WMI('NBT23276')

profiles = []

for up in c.Win32_UserProfile():
    profiles.append((up.LastUseTime, up.SID, up.LocalPath))

profiles.sort()

for p in profiles:
    print(p[0])
