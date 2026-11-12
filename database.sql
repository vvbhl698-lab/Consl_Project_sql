--
-- PostgreSQL database dump
--

\restrict vJ8SskPPt3OfPY1hqI1mbnQM2xg9sgkiDj9gUhWgaZTUXqSBnfDHTF12e3DeBjL

-- Dumped from database version 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1)
-- Dumped by pg_dump version 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: skill_status; Type: TYPE; Schema: public; Owner: vvbhl
--

CREATE TYPE public.skill_status AS ENUM (
    'Стажёр',
    'Новичёк',
    'Средний',
    'Опытный',
    'Профессионал'
);


ALTER TYPE public.skill_status OWNER TO vvbhl;

--
-- Name: task_status; Type: TYPE; Schema: public; Owner: vvbhl
--

CREATE TYPE public.task_status AS ENUM (
    'Новая',
    'Выполняется',
    'Заверешна'
);


ALTER TYPE public.task_status OWNER TO vvbhl;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: project_members; Type: TABLE; Schema: public; Owner: vvbhl
--

CREATE TABLE public.project_members (
    id integer NOT NULL,
    user_id integer NOT NULL,
    project_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.project_members OWNER TO vvbhl;

--
-- Name: project_members_id_seq; Type: SEQUENCE; Schema: public; Owner: vvbhl
--

CREATE SEQUENCE public.project_members_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.project_members_id_seq OWNER TO vvbhl;

--
-- Name: project_members_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vvbhl
--

ALTER SEQUENCE public.project_members_id_seq OWNED BY public.project_members.id;


--
-- Name: projects; Type: TABLE; Schema: public; Owner: vvbhl
--

CREATE TABLE public.projects (
    id integer NOT NULL,
    project character varying(20) NOT NULL,
    description text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT id_range CHECK (((id >= 1) AND (id <= 99999)))
);


ALTER TABLE public.projects OWNER TO vvbhl;

--
-- Name: projects_id_seq; Type: SEQUENCE; Schema: public; Owner: vvbhl
--

CREATE SEQUENCE public.projects_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.projects_id_seq OWNER TO vvbhl;

--
-- Name: projects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vvbhl
--

ALTER SEQUENCE public.projects_id_seq OWNED BY public.projects.id;


--
-- Name: tasks; Type: TABLE; Schema: public; Owner: vvbhl
--

CREATE TABLE public.tasks (
    id integer NOT NULL,
    project_id integer CONSTRAINT tasks_project_not_null NOT NULL,
    task character varying(20) NOT NULL,
    user_id integer CONSTRAINT tasks_name_not_null NOT NULL,
    status public.task_status NOT NULL,
    description text DEFAULT 'Не указанно'::text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT id_range CHECK (((id >= 1) AND (id <= 99999)))
);


ALTER TABLE public.tasks OWNER TO vvbhl;

--
-- Name: tasks_id_seq; Type: SEQUENCE; Schema: public; Owner: vvbhl
--

CREATE SEQUENCE public.tasks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tasks_id_seq OWNER TO vvbhl;

--
-- Name: tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vvbhl
--

ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;


--
-- Name: user_profiles; Type: TABLE; Schema: public; Owner: vvbhl
--

CREATE TABLE public.user_profiles (
    id integer NOT NULL,
    user_id integer NOT NULL,
    bio text DEFAULT 'Не указанно'::text,
    experience_level public.skill_status NOT NULL,
    github_username character varying(30) DEFAULT 'Не указанно'::character varying
);


ALTER TABLE public.user_profiles OWNER TO vvbhl;

--
-- Name: user_profiles_id_seq; Type: SEQUENCE; Schema: public; Owner: vvbhl
--

CREATE SEQUENCE public.user_profiles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_profiles_id_seq OWNER TO vvbhl;

--
-- Name: user_profiles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vvbhl
--

ALTER SEQUENCE public.user_profiles_id_seq OWNED BY public.user_profiles.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vvbhl
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    job_title character varying(30) NOT NULL,
    email character varying(30) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT id_max_5_digits CHECK (((id >= 1) AND (id <= 999999)))
);


ALTER TABLE public.users OWNER TO vvbhl;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: vvbhl
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO vvbhl;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vvbhl
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: project_members id; Type: DEFAULT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.project_members ALTER COLUMN id SET DEFAULT nextval('public.project_members_id_seq'::regclass);


--
-- Name: projects id; Type: DEFAULT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.projects ALTER COLUMN id SET DEFAULT nextval('public.projects_id_seq'::regclass);


--
-- Name: tasks id; Type: DEFAULT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);


--
-- Name: user_profiles id; Type: DEFAULT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.user_profiles ALTER COLUMN id SET DEFAULT nextval('public.user_profiles_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: project_members project_members_pkey; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.project_members
    ADD CONSTRAINT project_members_pkey PRIMARY KEY (id);


--
-- Name: projects projects_pkey; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id);


--
-- Name: projects projects_project_unique; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_project_unique UNIQUE (project);


--
-- Name: tasks tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);


--
-- Name: project_members unique_project_members; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.project_members
    ADD CONSTRAINT unique_project_members UNIQUE (user_id, project_id);


--
-- Name: projects unique_projects; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT unique_projects UNIQUE (project);


--
-- Name: tasks unique_tasks; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT unique_tasks UNIQUE (project_id, task);


--
-- Name: users unique_users; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT unique_users UNIQUE (name, job_title);


--
-- Name: user_profiles user_profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.user_profiles
    ADD CONSTRAINT user_profiles_pkey PRIMARY KEY (id);


--
-- Name: user_profiles user_profiles_user_id_key; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.user_profiles
    ADD CONSTRAINT user_profiles_user_id_key UNIQUE (user_id);


--
-- Name: users users_email_unique; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_unique UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: project_members project_members_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.project_members
    ADD CONSTRAINT project_members_project_id_fkey FOREIGN KEY (project_id) REFERENCES public.projects(id);


--
-- Name: project_members project_members_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.project_members
    ADD CONSTRAINT project_members_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: tasks tasks_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_name_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: tasks tasks_project_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_project_fkey FOREIGN KEY (project_id) REFERENCES public.projects(id);


--
-- Name: user_profiles user_profiles_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vvbhl
--

ALTER TABLE ONLY public.user_profiles
    ADD CONSTRAINT user_profiles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

\unrestrict vJ8SskPPt3OfPY1hqI1mbnQM2xg9sgkiDj9gUhWgaZTUXqSBnfDHTF12e3DeBjL

