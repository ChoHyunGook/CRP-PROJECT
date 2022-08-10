package crp.kr.api.soccer.repositories;

import crp.kr.api.soccer.domains.Player;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

/**
 * packageName:crp.kr.api.Soccer.repositories
 * fileName        :PlayerRepository
 * author           : chohyungook
 * date               :2022-05-19
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-19chohyungook최초 생성
 */
interface PlayerCustomRepository {
    //  000. 선수들의 키와 몸무게를 변경하시오.
    @Query(value = "update Player p set p.height = :height, p.weight = :weight where p.playerId = :playerId", nativeQuery = true)
    int update(@Param("height") String height, @Param("weight") String weight, @Param("playerId") String playerId);
}

@Repository
public interface PlayerRepository extends JpaRepository<Player, Long>, PlayerCustomRepository {
}
