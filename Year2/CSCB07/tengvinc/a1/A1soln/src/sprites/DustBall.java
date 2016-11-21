package sprites;

import game.Constants;

/**
 * A class that represents a dustball in the vacuum game.
 */
public class DustBall extends Dirt {
  /**
   * Creates a new <code>DustBall</code> that represents DustBall in the game.
   * 
   * @param row
   *          the row which this <code>DustBall</code> resides in now
   * @param column
   *          the column which this <code>DustBall</code> resides in now
   * @param value
   *          the score value of this <code>DustBall</code>
   */
  public DustBall(int row, int column, int value) {
    super(Constants.DUST_BALL, row, column, Constants.DUST_BALL_SCORE);
    // TODO Auto-generated constructor stub
  }

  /**
   * Move this <code>DustBall</code> to the parameter coordinate.
   * 
   * @param row
   *          the row which this <code>DustBall</code> is to be moved to
   * @param column
   *          the column which this <code>DustBall</code> is to be moved to
   *
   */
  public void moveTo(int row, int column) {
    this.updateCoordinates(row, column);
  }

}