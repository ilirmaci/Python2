class CashRegister:
    '''A cash register object.'''

    def __init__(self, loonies, toonies, fives, tens, twenties):
        '''(CashRegister, int, int, int, int, int) -> NoneType

        A CashRegister with loonies, toonies, fives, tens, and twenties.

        >>> register = CashRegister(5, 3, 2, 4, 6)
        >>> register.loonies
        5
        >>> register.toonies
        3
        >>> register.fives
        2
        >>> register.tens
        4
        >>> register.twenties
        6
        '''

        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def __eq__(self, other):
        '''(CashRegister, CashRegister) -> bool

        Return True iff total amount of cash in register self and
        register other is equal.
        
        >>> reg1 = CashRegister(2, 0, 0, 0, 0)
        >>> reg2 = CashRegister(0, 1, 0, 0, 0)
        >>> reg1 == reg2
        True
        '''
        return self.get_total() == other.get_total()

    def get_total(self):
        '''(CashRegister) -> int

        Return the total amount of cash in the register.
                
        >>> register = CashRegister(5, 5, 5, 5, 5)
        >>> register.get_total()
        190
        '''

        return self.loonies + 2*self.toonies + 5*self.fives + \
               10*self.tens + 20*self.twenties

    def add(self, count, denomination):
        '''(CashRegister, int, str) -> NoneType

        Adds count items of the denominations to the register.
        denomination is one of: loonies, toonies, fives, tens, twenties.
        
        >>> register = CashRegister(5, 5, 5, 5, 5)
        >>> register.add(2, 'toonies')
        >>> register.toonies
        7
        >>> register.add(1, 'tens')
        6
        '''

        if denomination == 'loonies':
            self.loonies += count
        elif denomination == 'toonies':
            self.toonies += count
        elif denomination == 'fives':
            self.fives += count
        elif denomination == 'tens':
            self.tens += count
        elif denomination == 'twenties':
            self.twenties += count

    def remove(self, count, denomination):
        '''(CashRegister, int, str) -> NoneType

        Remove count items of the denominations to the register.
        denomination is one of: loonies, toonies, fives, tens, twenties.
        
        >>> register = CashRegister(5, 5, 5, 5, 5)
        >>> register.remove(2, 'toonies')
        >>> register.toonies
        3
        >>> register.remove(1, 'tens')
        4
        '''

        if denomination == 'loonies':
            self.loonies -= count
        elif denomination == 'toonies':
            self.toonies -= count
        elif denomination == 'fives':
            self.fives -= count
        elif denomination == 'tens':
            self.tens -= count
        elif denomination == 'twenties':
            self.twenties -= count

if __name__ == "__main__":
    # A cash register with 5 loonies, 5 tootines, 5 fives,
    # 5 tens, and 5 twenties for a total of $190.

    register = CashRegister(5, 5, 5, 5, 5)
    print(register.get_total())

    register.add(3, 'toonies')
    register.remove(2, 'twenties')

    print(register.get_total())
    
