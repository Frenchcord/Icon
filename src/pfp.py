class pfp:
  def __init__(self, avatar_hash, id):
    self.hash = avatar_hash
    self.urlbase = f"https://cdn.discordapp.com/avatars/{id}/{avatar_hash}"
    self.png = self.url = f"{self.urlbase}.png"
    self.jepg = f'{self.urlbase}.jpeg'
    self.gif = f'{self.urlbase}.gif'
    self.webp = f'{self.urlbase}.webp'

  def taille(self, taille_: int):
    if not 16 > taille_ < 4096: raise ValueError(f'Taille minimum : 16 | taille maximum : 4096\nTaille reçut : {taille_}')
    return f'{self.url}?size={taille_}'

  def tout_format(self):
    slist = [f"{self.urlbase}.png", f'{self.urlbase}.jpeg', f'{self.urlbase}.gif', f'{self.urlbase}.webp']; liste = []
    for type in slist:
      for i in range(16, 4096): liste.append(f'{type}?size={i}')
    return liste

  def sformat(self, type: str, format: int):
    if not 16 > format < 4096: raise ValueError(f'Taille minimum : 16 | taille maximum : 4096\nTaille reçut : {format}')
    if type not in ['png', 'jpeg', 'gif', 'webp']: raise ValueError(f'Type invalide\nTypes supportés : png, jpeg, gif, webp\nType reçut : {type}')
    return f'{self.urlbase}.{type}?size={format}'

class guild_icon:
  def __init__(self, guild_hash, id):
    self.hash = guild_hash
    self.urlbase = f"https://cdn.discordapp.com/icons/{id}/{guild_hash}"
    self.png = self.url = f"{self.urlbase}.png"
    self.jepg = f'{self.urlbase}.jpeg'
    self.gif = f'{self.urlbase}.gif'
    self.webp = f'{self.urlbase}.webp'
    
  def taille(self, taille_: int):
    if not 16 > taille_ < 4096: raise ValueError(f'Taille minimum : 16 | taille maximum : 4096\nTaille reçut : {taille_}')
    return f'{self.url}?size={taille_}'

  def tout_format(self):
    slist = [f"{self.urlbase}.png", f'{self.urlbase}.jpeg', f'{self.urlbase}.gif', f'{self.urlbase}.webp']; liste = []
    for type in slist:
      for i in range(16, 4096): liste.append(f'{type}?size={i}')
    return liste

  def sformat(self, type: str, format: int):
    if not 16 > format < 4096: raise ValueError(f'Taille minimum : 16 | taille maximum : 4096\nTaille reçut : {format}')
    if type not in ['png', 'jpeg', 'gif', 'webp']: raise ValueError(f'Type invalide\nTypes supportés : png, jpeg, gif, webp\nType reçut : {type}')
    return f'{self.urlbase}.{type}?size={format}'

class invite_blackground:
  def __init__(self, guild_hash, id):
    self.hash = guild_hash
    self.urlbase = f"https://cdn.discordapp.com/splashes/{id}/{guild_hash}"
    self.png = self.url = f"{self.urlbase}.png"
    self.jepg = f'{self.urlbase}.jpeg'
    self.webp = f'{self.urlbase}.webp'
    
  def taille(self, taille_: int):
    if not 16 > taille_ < 4096: raise ValueError(f'Taille minimum : 16 | taille maximum : 4096\nTaille reçut : {taille_}')
    return f'{self.url}?size={taille_}'

  def tout_format(self):
    slist = [f"{self.urlbase}.png", f'{self.urlbase}.jpeg', f'{self.urlbase}.webp']; liste = []
    for type in slist:
      for i in range(16, 4096): liste.append(f'{type}?size={i}')
    return liste

  def sformat(self, type: str, format: int):
    if not 16 > format < 4096: raise ValueError(f'Taille minimum : 16 | taille maximum : 4096\nTaille reçut : {format}')
    if type not in ['png', 'jpeg', 'webp']: raise ValueError(f'Type invalide\nTypes supportés : png, jpeg, webp\nType reçut : {type}')
    return f'{self.urlbase}.{type}?size={format}'

class splash_dec:
  def __init__(self, guild_hash, id):
    self.hash = guild_hash
    self.urlbase = f"https://cdn.discordapp.com/discovery-splashes/{id}/{guild_hash}"
    self.png = self.url = f"{self.urlbase}.png"
    self.jepg = f'{self.urlbase}.jpeg'
    self.webp = f'{self.urlbase}.webp'
    
  def taille(self, taille_: int):
    if not 16 > taille_ < 4096: raise ValueError(f'Taille minimum : 16 | taille maximum : 4096\nTaille reçut : {taille_}')
    return f'{self.url}?size={taille_}'

  def tout_format(self):
    slist = [f"{self.urlbase}.png", f'{self.urlbase}.jpeg', f'{self.urlbase}.webp']; liste = []
    for type in slist:
      for i in range(16, 4096): liste.append(f'{type}?size={i}')
    return liste

  def sformat(self, type: str, format: int):
    if not 16 > format < 4096: raise ValueError(f'Taille minimum : 16 | taille maximum : 4096\nTaille reçut : {format}')
    if type not in ['png', 'jpeg', 'webp']: raise ValueError(f'Type invalide\nTypes supportés : png, jpeg, webp\nType reçut : {type}')
    return f'{self.urlbase}.{type}?size={format}'

class banner:
  def __init__(self, avatar_hash, id):
    self.hash = avatar_hash
    self.urlbase = f"https://cdn.discordapp.com/banners/{id}/{avatar_hash}"
    self.png = self.url = f"{self.urlbase}.png"
    self.jepg = f'{self.urlbase}.jpeg'
    self.gif = f'{self.urlbase}.gif'
    self.webp = f'{self.urlbase}.webp'

  def taille(self, taille_: int):
    if not 16 > taille_ < 4096: raise ValueError(f'Taille minimum : 16 | taille maximum : 4096\nTaille reçut : {taille_}')
    return f'{self.url}?size={taille_}'

  def tout_format(self):
    slist = [f"{self.urlbase}.png", f'{self.urlbase}.jpeg', f'{self.urlbase}.gif', f'{self.urlbase}.webp']; liste = []
    for type in slist:
      for i in range(16, 4096): liste.append(f'{type}?size={i}')
    return liste
