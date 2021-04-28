class catat:
  def __init__(self, *args, **kwargs):
      self.bab = kwargs.get('bab')
      self.grammar = kwargs.get('grammar')
      self.vocab = kwargs.get('vocab')
      self.arti = kwargs.get('arti')

  def __repr__(self):
      return 'Bab ' + str(self.bab) + '\n Grammar : '+ self.grammar + '\n Vocab   : '+ self.vocab + '\n Arti    : '+ self.arti

catatan ={}

def input_catatan():
    print('Monggo diisi ya')
    input_bab = int(input('Bab          :'))
    input_grammar = input('Grammar      :')
    input_vocab = input('Vocabulary   :')
    input_arti = input('Meaning      :')

    catatan[input_bab] = catat(
        bab = input_bab,
        grammar = input_grammar,
        vocab = input_vocab,
        arti = input_arti
    )
    print('\n오케이 만따뿌 지와')

def lihat_catatan():
    for i in catatan.keys():
        print(catatan[i])
        print()
    
def hapus_catatan():
    print('Mau hapus bab berapa?')
    n = int(input('>> '))
    copyan = catatan.copy()

    for i in copyan.keys():
        if i == n:
            y = catatan.pop(i)
    print('Okeh sudah dihapus')
    return y

while True:
    print('---------------------------------------------------')
    print('Selamat datang di tempat nyatet, silahkan pilih menu')
    print('1. Input catatan')
    print('2. Lihat catatan')
    print('3. Hapus catatan')
    print('4. Cukup belajarnya ya')
    print('---------------------------------------------------')

    n = int(input('>> '))
    if n == 1:
        input_catatan()
    elif n == 2:
        lihat_catatan()
    elif n ==3:
        hapus_catatan()
    else:
        print('Oke Bye')
        break
