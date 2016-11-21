def __str__(self):
    '''(Matrix) -> str
    Return the string representation of this node
    '''
    ret_str = 'N'
    h_cur = self._head
    # Form the index Nodes
    # For loop through horizontal dimension
    for j in range(0, self._h_dim+1):
        if h_cur != None:
            h_cur = h_cur.get_right()
        if h_cur == None or h_cur.get_contents() > j:
            ret_str += '-----'
        else:
            ret_str += '----'+ str(h_cur.get_contents())
    v_cur = self._head
    for i in range(0, self._v_dim+1):
        # Print vertical bars for visual identitification
        ret_str = ret_str + "\n" + "|"
        for j in range(0, self._h_dim+1):
            ret_str += "    |"
        ret_str += "\n"
        # Traverse to and from each vertical index node
        if v_cur:
            v_cur = v_cur.get_down()
        if not v_cur or v_cur.get_contents() > i:
            ret_str += '|'
        else:
            ret_str += str(v_cur.get_contents())
            cont_cur = v_cur
            for x in range(0, self._h_dim+1):
                if self.get_val(i, x) != 0:
                    ret_str += '----'+ str(self.get_val(i, x))
                else:
                    ret_str += '----|'
    return ret_str