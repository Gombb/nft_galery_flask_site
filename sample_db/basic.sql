--
-- PostgreSQL database dump
--

-- Dumped from database version 12.7 (Ubuntu 12.7-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.7 (Ubuntu 12.7-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: artist; Type: TABLE; Schema: public; Owner: gombb
--

CREATE TABLE public.artist (
    id integer NOT NULL,
    name character varying,
    bio character varying,
    avatar_url character varying
);


ALTER TABLE public.artist OWNER TO gombb;

--
-- Name: artist_id_seq; Type: SEQUENCE; Schema: public; Owner: gombb
--

CREATE SEQUENCE public.artist_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.artist_id_seq OWNER TO gombb;

--
-- Name: artist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: gombb
--

ALTER SEQUENCE public.artist_id_seq OWNED BY public.artist.id;


--
-- Name: collectible; Type: TABLE; Schema: public; Owner: gombb
--

CREATE TABLE public.collectible (
    id integer NOT NULL,
    contract_address character varying NOT NULL,
    token_id character varying NOT NULL,
    artist_id integer NOT NULL
);


ALTER TABLE public.collectible OWNER TO gombb;

--
-- Name: collectible_id_seq; Type: SEQUENCE; Schema: public; Owner: gombb
--

CREATE SEQUENCE public.collectible_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.collectible_id_seq OWNER TO gombb;

--
-- Name: collectible_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: gombb
--

ALTER SEQUENCE public.collectible_id_seq OWNED BY public.collectible.id;


--
-- Name: artist id; Type: DEFAULT; Schema: public; Owner: gombb
--

ALTER TABLE ONLY public.artist ALTER COLUMN id SET DEFAULT nextval('public.artist_id_seq'::regclass);


--
-- Name: collectible id; Type: DEFAULT; Schema: public; Owner: gombb
--

ALTER TABLE ONLY public.collectible ALTER COLUMN id SET DEFAULT nextval('public.collectible_id_seq'::regclass);


--
-- Data for Name: artist; Type: TABLE DATA; Schema: public; Owner: gombb
--

COPY public.artist (id, name, bio, avatar_url) FROM stdin;
1	Apemaster	Master of all apes.	https://www.jcu.edu.au/__data/assets/image/0004/654853/Orangutan-Tapanuli-Maxime-Aliaga-77.jpeg
\.


--
-- Data for Name: collectible; Type: TABLE DATA; Schema: public; Owner: gombb
--

COPY public.collectible (id, contract_address, token_id, artist_id) FROM stdin;
1	0xA0F38233688bB578c0a88102A95b846c18bc0bA7	3284	1
\.


--
-- Name: artist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: gombb
--

SELECT pg_catalog.setval('public.artist_id_seq', 1, false);


--
-- Name: collectible_id_seq; Type: SEQUENCE SET; Schema: public; Owner: gombb
--

SELECT pg_catalog.setval('public.collectible_id_seq', 1, false);


--
-- Name: artist artist_pk; Type: CONSTRAINT; Schema: public; Owner: gombb
--

ALTER TABLE ONLY public.artist
    ADD CONSTRAINT artist_pk PRIMARY KEY (id);


--
-- Name: artist_id_uindex; Type: INDEX; Schema: public; Owner: gombb
--

CREATE UNIQUE INDEX artist_id_uindex ON public.artist USING btree (id);


--
-- Name: collectible fk_artist; Type: FK CONSTRAINT; Schema: public; Owner: gombb
--

ALTER TABLE ONLY public.collectible
    ADD CONSTRAINT fk_artist FOREIGN KEY (artist_id) REFERENCES public.artist(id);


--
-- PostgreSQL database dump complete
--

