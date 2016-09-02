class LightSwitch():
    '''A class which represents a light switch that is either 'on' or 'off
    '''

    def __init__(self, state):
        ''' (LightSwitch, str) -> NoneType
        Creates a LightSwitch with state as its starting state. True
        corresponds to 'on', False corresponds to 'off'.
        '''
        if (state == "on"):
            self._state = True
        elif (state == "off"):
            self._state = False

    def __str__(self):
        '''(LightSwitch) -> str
        Returns a LightSwitch's current state
        '''
        if (self._state):
            return "I am on"
        else:
            return "I am off"

    def turn_on(self):
        '''(LightSwitch) -> NoneType
        Changes  a given LightSwitch's state to 'on'
        '''
        self._state = True

    def turn_off(self):
        '''(LightSwitch) -> NoneType
        Changes a given LightSwitch's state to 'off'
        '''
        self._state = False

    def flip(self):
        '''(light_Switch) -> NoneType
        Changes a given LightSwitch's state to the opposite of what it
        previously possessed (if it began as 'off' it will become 'on' and
        vice versa
        '''
        self._state = not self._state

    def get_state(self):
        '''(LightSwitch) -> bool
        Returns a given LightSwitch's state as a boolean. True being that
        the switch is 'on', false being that the switch is 'off'
        '''
        return self._state


class SwitchBoard():
    ''' A class which represents a switch board containing LightSwtiches
    '''

    def __init__(self, num_switches):
        '''(SwitchBoard, int) -> NoneType
        Create a SwitchBoard with num_switches LightSwitches; all of which
        are initialized as 'off'
        '''
        # num_switches of LightSwitch are intialized as 'off' and stored as
        # elements in a list of the created SwitchBoard
        self._switches = []
        for i in range(num_switches):
            new_switch = LightSwitch("off")
            self._switches.append(new_switch)

    def __str__(self):
        '''(SwitchBoard) -> str
        Returns the index of LightSwitches that are 'on' in a given
        SwitchBoard
        '''
        # Call upon which_switch method to retrieve the list of LightSwitches
        # that are 'on'
        ret_str = "The following switches are on: "
        for i in self.which_switch():
            ret_str = ret_str + str(i) + " "
        return ret_str

    def which_switch(self):
        '''(SwitchBoard) -> list of int
        Returns a list of integers. The integers correspond to indices of
        LightSwitches within the given SwitchBoard that are on.
        '''
        # For loop through the list of switches and retrieve the state of each
        # switch. If the switch is on (returns True) include the index of
        # that switch into the returned
        ret_list = []
        for i in range(len(self._switches)):
            if(self._switches[i].get_state()):
                ret_list.append(i)
        return ret_list

    def flip(self, n):
        '''(SwitchBoard, int) -> NoneType
        Given the index of a LightSwitch in a SwitchBoard, change the state of
        that LightSwitch
        '''
        if(n <= len(self._switches) and n >= 0):
            self._switches[n].flip()

    def flip_every(self, n):
        '''(SwitchBoard, int) -> NoneType
        Switch the state of every n'th lightswitch starting at 0.
        '''
        # For loop through the list of LightSwitches in the given SwitchBoard
        # in iterations of n. To prevent program error, n can neither be a
        # value that is outside the ranage of self._switches nor <= 0
        if(n <= len(self._switches) and n > 0):
            for i in range(0, len(self._switches), n):
                self.flip(i)

    def reset(self):
        '''(SwitchBoard) -> NoneType
        Turn off all LightSwitches in a Switchboard.
        '''
        # For loops through the list of LightSwitches in the given SwitchBoard
        # and call upon the turn_off method of each of these LightSwitches
        for i in range(len(self._switches)):
            self._switches[i].turn_off()


# Answerto Light Switch problem: Only light switches where the index are
# perfect squares (and 0) remain on
# The reason is as following:
# Each switch will be flipped the same number of times as the number of factors
# it possesses between 1 and 1023
# If a switch is flipped an even number of times it will remain 'off' at the
# end. Conversely, a switch that is fipped an odd number of times will remain
# 'on' at the end.
# The only integers capable of possessing an odd number of unique factors are
# 0, 1, and all perfect squares (all factors of a number require a coefficient
# different from itself so as to result in the product of the original number.
# The exception to this are perfect squares where its root acts as its factor
# "twice")
#
# Below is the code used to test the result

if __name__ == '__main__':
    s = SwitchBoard(1024)
    for i in range(1024):
        s.flip_every(i)
    print(s)
