package crp.kr.api.soccer.services;

import crp.kr.api.soccer.domains.Stadium;
import crp.kr.api.soccer.repositories.StadiumRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

/**
 * packageName:crp.kr.api.Soccer.services
 * fileName        :StadiumServiceImpl
 * author           : chohyungook
 * date               :2022-05-19
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-19chohyungook최초 생성
 */
@Service
@RequiredArgsConstructor
public class StadiumServiceImpl implements StadiumService{
    private final StadiumRepository repository;

    @Override
    public List<Stadium> findAll() {
        return repository.findAll();
    }

    @Override
    public List<Stadium> findAll(Sort sort) {
        return repository.findAll(sort);
    }

    @Override
    public Page<Stadium> findAll(Pageable pageable) {
        return repository.findAll(pageable);
    }

    @Override
    public long count() {
        return repository.count();
    }

    @Override
    public String delete(Stadium stadium) {
        repository.delete(stadium);
        return null;
    }

    @Override
    public String save(Stadium stadium) {
        repository.save(stadium);
        return null;
    }

    @Override
    public Optional<Stadium> findById(Long stadiumNo) {
        return repository.findById(stadiumNo);
    }

    @Override
    public boolean existsById(Long stadiumNo) {
        return repository.existsById(stadiumNo);
    }
}
