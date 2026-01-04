from dataclasses import dataclass


@dataclass
class JobApplication:
    id: str
    title: str
    location: str
    company: str
    salary_range: dict[str, int]  # keys: "high_end" and "low_end"
    status: str
    expiration: int
    links: list[str]
    priority: int
    created_at: float  # timestamp
    updated_at: float  # timestamp
