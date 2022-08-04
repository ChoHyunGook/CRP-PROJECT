package crp.kr.api.board.repositories;

import crp.kr.api.board.domains.Board;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * packageName:crp.kr.api.repositories
 * fileName        :BoardRepository
 * author           : chohyungook
 * date               :2022-05-04
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-04chohyungook최초 생성
 */
@Repository
public interface BoardRepository extends JpaRepository<Board,Long>{
}
