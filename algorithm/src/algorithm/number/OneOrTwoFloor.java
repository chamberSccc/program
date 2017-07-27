package algorithm.number;

import java.io.*;
import java.util.*;

public class OneOrTwoFloor {
    public static void main(String[] args) {
        OneOrTwoFloor oneOrTwoFloor = new OneOrTwoFloor();
        int a = oneOrTwoFloor.upstair(10);
        System.out.println(a);

    }
    static Set<List> resultSet = new HashSet<List>();
    int index = 0;

    //定义阈值
    private final int threshold = 2000;
    private int upstair(int n){
        int sum = 0;
        for (int i = 0; i < threshold; i++) {
            List<Integer> list = new ArrayList<Integer>();
            for (int j = 0; j < n; j++) {
                int ranNum = (int) (Math.random()*2 + 1);
                list.add(ranNum);
                sum += ranNum;
                if (sum == n){
                    sum = 0;
                    try {
                        List<Integer> temp = deepCopy(list);
                        resultSet.add(temp);
                    } catch (IOException e) {
                        e.printStackTrace();
                    } catch (ClassNotFoundException e) {
                        e.printStackTrace();
                    }
                    list.clear();
                    break;
                }else if(sum >n){
                    sum = 0;
                    break;
                }
            }
        }
        int size = resultSet.size();
        return size;
    }
    public static <T> List<T> deepCopy(List<T> src) throws IOException, ClassNotFoundException {
        ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
        ObjectOutputStream out = new ObjectOutputStream(byteOut);
        out.writeObject(src);

        ByteArrayInputStream byteIn = new ByteArrayInputStream(byteOut.toByteArray());
        ObjectInputStream in = new ObjectInputStream(byteIn);
        @SuppressWarnings("unchecked")
        List<T> dest = (List<T>) in.readObject();
        return dest;
    }



}
