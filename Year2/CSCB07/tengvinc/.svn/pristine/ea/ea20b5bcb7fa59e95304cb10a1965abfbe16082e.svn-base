package sprites;

/**
 * A class that represents the dirt of the vacuum game.
 */
public abstract class Dirt extends Sprite {
  private int value; // score value of this dirt

  /**
   * Creates a new <code>Dirt</code> that represents Dirt in the game.
   * 
   * @param symbol
   *          the symbol that depicts this <code>Dirt</code>
   * @param row
   *          the row which this <code>Dirt</code> resides in now
   * @param column
   *          the column which this <code>Dirt</code> resides in now
   * @param value
   *          the score value of this <code>Dirt</code>
   */
  public Dirt(char symbol, int row, int column, int value) {
    super(symbol, row, column);
    // TODO Auto-generated constructor stub
  }

  /**
   * Returns the score value of this <code>Dirt</code>.
   * 
   * @return value: the score value of this <code>Dirt</code>
   */
  public int getValue() {
    return value;
  }

  @Override
  public int hashCode() {
    final int prime = 31;
    int result = super.hashCode();
    result = prime * result + value;
    return result;
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj) {
      return true;
    }
    if (!super.equals(obj)) {
      return false;
    }
    if (getClass() != obj.getClass()) {
      return false;
    }
    Dirt other = (Dirt) obj;
    if (value != other.value) {
      return false;
    }
    return true;
  }

}
