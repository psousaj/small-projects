package com.dev.psousaj.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.dev.psousaj.model.Course;

@Repository
public interface CourseRepository extends JpaRepository<Course, Long>{
    public Course findByName(String name);
}
