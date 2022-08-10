package crp.kr.api.soccer.repositories;

import crp.kr.api.soccer.domains.Stadium;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

/**
 * packageName:crp.kr.api.Soccer.repositories
 * fileName        :SoccerRepository
 * author           : chohyungook
 * date               :2022-05-09
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-09chohyungook최초 생성
 */
interface StadiumCustomRepository {
    //  000. 스타디움 전화번호 tel 을 변경하도록 하시오.
    @Query(value = "update Stadium s set s.tel = :tel where s.stadiumId = :stadiumId", nativeQuery = true)
    int update(@Param("tel") String tel, @Param("stadiumId") String stadiumId);
}

@Repository
public interface StadiumRepository extends JpaRepository<Stadium, Long>, StadiumCustomRepository {
}
