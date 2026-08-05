FROM debian:bookworm-slim
RUN useradd --create-home --uid 10001 sandbox
USER sandbox
WORKDIR /workspace
CMD ["bash"]
