---
title: "shared_memory_ipc.cpp"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/aesc/shared_memory_ipc.cpp.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

//
========================================================================
======
// Android NDK Zero-Copy ASharedMemory & Abstract Domain Socket IPC
// Bypasses Android 1MB Binder limit to stream token matrices to Snapdragon NPU
//
========================================================================
======
#include <android/sharedmem.h>
#include <sys/mman.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <cstring>
#include <iostream>

int create_shared_tensor_pool(const char* pool_name, size_t buffer_size) {
    int fd = ASharedMemory_create(pool_name, buffer_size);
    if (fd < 0) return -1;

    void* local_buffer = mmap(NULL, buffer_size, PROT_READ | PROT_WRITE,
MAP_SHARED, fd, 0);
    if (local_buffer == MAP_FAILED) {
        close(fd);
        return -1;
    }

    std::strcpy(static_cast<char*>(local_buffer), "INIT_NPU_STREAM");
    ASharedMemory_setProt(fd, PROT_READ);
    return fd;
}

int send_fd_over_unix_socket(int socket_fd, int fd_to_send) {
    struct msghdr msg = {0};
    char buf[CMSG_SPACE(sizeof(int))];
    memset(buf, 0, sizeof(buf));

    struct iovec io = { .iov_base = (void*)"FD", .iov_len = 2 };
    msg.msg_iov = &io;
    msg.msg_iovlen = 1;
    msg.msg_control = buf;
    msg.msg_controllen = sizeof(buf);



    struct cmsghdr* cmsg = CMSG_FIRSTHDR(&msg);
    cmsg->cmsg_level = SOL_SOCKET;
    cmsg->cmsg_type = SCM_RIGHTS;
    cmsg->cmsg_len = CMSG_LEN(sizeof(int));
    memcpy(CMSG_DATA(cmsg), &fd_to_send, sizeof(int));

    return sendmsg(socket_fd, &msg, 0);
}
