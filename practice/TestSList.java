import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Created by EuiJeong Chung on 2/14/17.
 */

public class TestSList {
    @Test
    public void test() {
        SList sl = new SList();
        SList sl2 = new SList();
        sl.insertFront(1);
        assertEquals(-1, sl2.getFront());
    }
}
