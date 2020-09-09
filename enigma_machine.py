class Rotor:
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, notch, name):
        self.setting = [['A', a], ['B', b], ['C', c], ['D', d], ['E', e], ['F', f], ['G', g], ['H', h], ['I', i], ['J', j], ['K', k], ['L', l], ['M', m], ['N', n], ['O', o], ['P', p], ['Q', q], ['R', r], ['S', s], ['T', t], ['U', u], ['V', v], ['W', w], ['X', x], ['Y', y], ['Z', z]]
        self.notch = notch
        self.name = name
        #print("Rotor made.\n")
        
    def get(self, key):
        index = ord(key.upper()[0]) - 65
        return self.setting[index][1]
    
    def getr(self, key):
        for i in range(0, len(self.setting)):
            if key == self.setting[i][1]:
                return chr(i + 65)
    
    def rotate(self):
        temp_pair = self.setting.pop(0)
        self.setting.append(temp_pair)
        if temp_pair[0] == self.notch:
            return True
        else:
            return False
        
    def reset_rotation(self):
        while self.setting[0][0] != 'A':
            self.rotate()
        
    def set_rotation(self, rotation_setting):
        self.reset_rotation()
        while rotation_setting > 0:
            self.rotate()
            rotation_setting -= 1
            
    def get_name(self):
        return self.name
        
class Plugboard:
    def __init__(self):
        self.connections = []
        #print("Plugboard made.\n")
        
    def make_connection(self, letter_1, letter_2):
        for connection in self.connections:
            if connection[0] == letter_1 or connection[0] == letter_2 or connection[1] == letter_1 or connection[1] == letter_2:
                print("One of the letters are already connected.")
        self.connections.append([letter_1, letter_2])
        print("Connection Made.")
        
    def remove_connection(self, key):
        for i in range(0, len(self.connections)):
            if self.connections[i][0] == key or self.connections[i][1] == key:
                print("Removed connection: " + self.connections.pop(i))
                
    def print_connections(self):
        print(self.connections)
        
    def remove_all_connections(self):
        self.connections.clear()
        print("Removed all connections.")
        
    def get(self, key):
        for connection in self.connections:
            if connection[0] == key:
                return connection[1]
            if connection[1] == key:
                return connection[0]
        return key
    
    def getr(self, key):
        for connection in self.connections:
            if connection[1] == key:
                return connection[0]
            if connection[0] == key:
                return connection[1]
        return key
        
class Reflector:
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
        self.setting = [['A', a], ['B', b], ['C', c], ['D', d], ['E', e], ['F', f], ['G', g], ['H', h], ['I', i], ['J', j], ['K', k], ['L', l], ['M', m], ['N', n], ['O', o], ['P', p], ['Q', q], ['R', r], ['S', s], ['T', t], ['U', u], ['V', v], ['W', w], ['X', x], ['Y', y], ['Z', z]]
        #print("Reflector made.\n")
        
    def get(self, key):
        index = ord(key.upper()[0]) - 65
        return self.setting[index][1]
            
class EnigmaMachine:
    def __init__(self):
        print("\nWELCOME TO THE ENIGMA MACHINE\n")
        self.rotor_set = []
        self.setup_rotors()
        self.plugboard = Plugboard()
        self.setup_reflector()
        cont = True
        while cont:
            print("1. Use")
            print("2. Quit")
            sel = input("Select an option: ")
            if sel == "1":
                self.use()
            elif sel == "2":
                cont = False
        
    def setup_rotors(self):
        s = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        notch = "Q"
        name = "I"
        self.rotor_set.append(Rotor(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14], s[15], s[16], s[17], s[18], s[19], s[20], s[21], s[22], s[23], s[24], s[25], notch, name))
        s = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        notch = "E"
        name = "II"
        self.rotor_set.append(Rotor(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14], s[15], s[16], s[17], s[18], s[19], s[20], s[21], s[22], s[23], s[24], s[25], notch, name))
        s = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        notch = "V"
        name = "III"
        self.rotor_set.append(Rotor(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14], s[15], s[16], s[17], s[18], s[19], s[20], s[21], s[22], s[23], s[24], s[25], notch, name))
        s = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
        notch = "J"
        name = "IV"
        self.rotor_set.append(Rotor(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14], s[15], s[16], s[17], s[18], s[19], s[20], s[21], s[22], s[23], s[24], s[25], notch, name))
        s = "VZBRGITYUPSDNHLXAWMJQOFECK"
        notch = "Z"
        name = "V"
        self.rotor_set.append(Rotor(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14], s[15], s[16], s[17], s[18], s[19], s[20], s[21], s[22], s[23], s[24], s[25], notch, name))
        
    def setup_reflector(self):
        s = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        self.reflector = Reflector(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14], s[15], s[16], s[17], s[18], s[19], s[20], s[21], s[22], s[23], s[24], s[25])
        
    def use(self):
        print("\nAvailable Rotors:")
        self.print_rotors()
        ra = input("Select the 1st rotor: ")
        while not self.is_valid_rotor(ra, "0", "0"):
            ra = input("Select the 1st rotor from one of the options: ")
        rb = input("Select the 2nd rotor: ")
        while not self.is_valid_rotor(rb, ra, "0"):
            ra = input("Select the 2nd rotor from one of the options: ")
        rc = input("Select the 3rd rotor: ")
        while not self.is_valid_rotor(rc, ra, rb):
            rc = input("Select the 3rd rotor from one of the options: ")
        rna = input("Select the 1st rotor's rotation setting: ")
        while not self.is_valid_setting(rna):
            rna = input("Select the 1st rotor's rotation setting(1 - 26): ")
        rnb = input("Select the 2nd rotor's rotation setting: ")
        while not self.is_valid_setting(rnb):
            rna = input("Select the 2nd rotor's rotation setting(1 - 26): ")
        rnc = input("Select the 3rd rotor's rotation setting: ")
        while not self.is_valid_setting(rnc):
            rnc = input("Select the 3rd rotor's rotation setting(1 - 26): ")
        rotor_a = self.rotor_set[int(ra) - 1]
        rotor_b = self.rotor_set[int(rb) - 1]
        rotor_c = self.rotor_set[int(rc) - 1]
        rotor_a.set_rotation(int(rna))
        rotor_b.set_rotation(int(rnb))
        rotor_c.set_rotation(int(rnc))
        print("\nThe current plugboard connections are: ", end = "")
        self.plugboard.print_connections()
        change = input("Would you like to change the plugboard connections?(y/n): ")
        if change == "y":
            self.plugboard.remove_all_connections
            connection = input("Make a connection(ab) or enter \".\" to stop: ").upper()
            while connection != ".":
                self.plugboard.make_connection(connection[0], connection[1])
                connection = input("Make a connection(ab) or enter \".\" to stop: ").upper()
        response = input("Enter text to encrypt/decrypt \".\" to stop: ").upper().replace(" ", "")
        while response != ".":
            for char in response:
                if char.isalpha():
                    rotate_next = rotor_a.rotate()
                    if rotate_next:
                        rotate_next = rotor_b.rotate()
                        if rotate_next:
                            rotor_c.rotate()
                    char = self.plugboard.get(char)
                    char = rotor_a.get(char)
                    char = rotor_b.get(char)
                    char = rotor_c.get(char)
                    char = self.reflector.get(char)
                    char = rotor_c.getr(char)
                    char = rotor_b.getr(char)
                    char = rotor_a.getr(char)
                    char = self.plugboard.getr(char)
                    print(char, end='')
            response = input("\nEnter text to encrypt/decrypt \".\" to stop: ").upper()
        
    def print_rotors(self):
        for i in range(0, len(self.rotor_set)):
            print(str(i + 1) + ". " + self.rotor_set[i].get_name())
            
    def is_valid_rotor(self, stringA, stringB, stringC):
        try:
            number = int(stringA)
            if number > len(self.rotor_set) or number < 1:
                return False
            if number == int(stringB) or number == int(stringC):
                return False
            return True
        except:
            return False
        
    def is_valid_setting(self, stringA):
        try:
            number = int(stringA)
            if number < 1 or number > 26:
                return False
            return True
        except:
            return False
    
def main():
    enigma_machine = EnigmaMachine()
        
if __name__ == '__main__':
    main()
