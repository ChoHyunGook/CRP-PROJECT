package crp.kr.api.soccer.services;

import crp.kr.api.soccer.domains.Schedule;
import crp.kr.api.soccer.repositories.ScheduleRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

/**
 * packageName:crp.kr.api.Soccer.repositories
 * fileName        :SoccerServiceImpl
 * author           : chohyungook
 * date               :2022-05-09
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-09chohyungook최초 생성
 */
@Service
@RequiredArgsConstructor
public class ScheduleServiceImpl implements ScheduleService{
    private final ScheduleRepository repository;

    @Override
    public List<Schedule> findAll() {
        return repository.findAll();
    }

    @Override
    public List<Schedule> findAll(Sort sort) {
        return repository.findAll(sort);
    }

    @Override
    public Page<Schedule> findAll(Pageable pageable) {
        return repository.findAll(pageable);
    }

    @Override
    public long count() {
        return repository.count();
    }

    @Override
    public String delete(Schedule schedule) {
        repository.delete(schedule);
        return null;
    }

    @Override
    public String save(Schedule schedule) {
        repository.save(schedule);
        return null;
    }

    @Override
    public Optional<Schedule> findById(Long scheduleNo) {
        return repository.findById(scheduleNo);
    }

    @Override
    public boolean existsById(Long scheduleNo) {
        return repository.existsById(scheduleNo);
    }
}
