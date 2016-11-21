package sprites;

import game.Constants;

public class Vacuum extends Sprite {
  private int score; // starting score of this Vacuum
  private int capacity; // starting capacity of this Vacuum
  private int fullness; // max capacity of this Vacuum
  private Sprite under; // the sprite to which this Vacuum resides on top of

  /**
   * Creates a new <code>Vacuum</code> that represents Vacuum in the game.
   * 
   * @param symbol
   *          the symbol that depicts this <code>Vacuum</code>
   * @param row
   *          the row which this <code>Vacuum</code> resides in now
   * @param column
   *          the column which this <code>Vacuum</code> resides in now
   * @param capacity
   *          the starting capacity of this <code>Vacuum</code>
   */
  public Vacuum(char symbol, int row, int column, int capacity) {
    super(symbol, row, column);
    this.capacity = Constants.CAPACITY;
    this.fullness = Constants.EMPTY;
    // TODO Auto-generated constructor stub
  }

  /**
   * Changes the coordinate of the vacuum to the parameter row and column.
   * 
   * @param row
   *          the row which this <code>Vacuum will move to</code>
   * @param column
   *          the column which this <code>Vacuum</code> will move to
   */
  public void moveTo(int row, int column) {
    this.updateCoordinates(row, column);
  }

  /**
   * Attempts to clean the given cell.If the vacuum is not full, increase its
   * fullness and score by appropriate values, else do not clean the cell.
   * Return whether or no the cell has been cleaned.
   * 
   * @param score
   *          the score value of the dirt that <code>Vacuum</code> is on top of
   * @return whether or not the cell has been cleaned
   */
  public boolean clean(int score) {
    if (this.fullness < this.capacity) {
      if (this.getUnder() instanceof Dirt) {
        this.score += score;
        this.fullness += Constants.FULLNESS_INC;
        return true;
      }

    }
    return false;
  }

  /**
   * Return the object currently under this vacuum.
   * 
   * @return the object currently under this vacuum
   */
  public Sprite getUnder() {
    // TODO Auto-generated method stub
    return under;
  }

  /**
   * Sets the sprite to which this vacuum currently resides on top of.
   * 
   * @param under
   *          the sprite below this vacuum
   */
  public void setUnder(Sprite under) {
    this.under = under;
  }

  /**
   * Return the score of this vacuum.
   * 
   * @return the score of this vacuum
   */
  public int getScore() {
    return score;
  }

  /**
   * Empties the vacuum.
   * 
   */
  public void empty() {
    fullness = Constants.EMPTY;
  }

}
