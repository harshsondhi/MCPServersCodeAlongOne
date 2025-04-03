package com.harsh.sondhi.demoMCPServerone;

import org.springframework.ai.tool.ToolCallback;
import org.springframework.ai.tool.ToolCallbacks;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.util.List;

@SpringBootApplication
public class DemoMcpServeroneApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoMcpServeroneApplication.class, args);
	}

	@Bean
	public List<ToolCallback> harshTools(CourseService courseService) {
		 return List.of(ToolCallbacks.from(courseService));
	}
}
