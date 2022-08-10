package crp.kr.api.common.dataStructure;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.RequiredArgsConstructor;

import java.util.Map;
import java.util.Scanner;

/**
 * packageName:crp.kr.api.common.dataStructure
 * fileName        :ItemCRUD
 * author           : chohyungook
 * date               :2022-05-10
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-10chohyungook최초 생성
 */
public class ItemCRUD {
    public static void main(String[] args) {
    }
}
@Data @AllArgsConstructor
class Item{
    private int id;
    private String name;
    private int price;
}
interface ItemService{
}
@RequiredArgsConstructor
class ItemServiceImpl implements ItemService{
}